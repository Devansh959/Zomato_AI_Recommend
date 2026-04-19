import os
import sqlite3
import pandas as pd
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None
    print("WARNING: GROQ_API_KEY not found in .env file.")

df_restaurants = pd.DataFrame()

def get_clean_dataframe():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'zomato.sqlite')
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql('SELECT * FROM restaurants', conn)
    
    df['clean_rate'] = df['rate'].astype(str).str.extract(r'(\d+\.\d+)').astype(float)
    df['clean_cost'] = df['approx_cost(for_two_people)'].astype(str).str.replace(',', '').str.extract(r'(\d+)').astype(float)
    df['clean_votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0)
    
    return df

@asynccontextmanager
async def lifespan(app: FastAPI):
    global df_restaurants
    try:
        print("Loading and cleaning restaurant dataset into memory...")
        df_restaurants = get_clean_dataframe()
        print(f"Loaded {len(df_restaurants)} restaurants.")
    except Exception as e:
        print(f"Failed to load dataset: {e}")
    yield
    df_restaurants = pd.DataFrame()

app = FastAPI(title="Zomato Recommender API", lifespan=lifespan)

class UserPreferences(BaseModel):
    location: Optional[str] = None
    max_budget: Optional[float] = None
    cuisine: Optional[str] = None
    min_rating: Optional[float] = None
    additional_preferences: Optional[str] = None

@app.get("/api/locations")
def get_locations():
    if df_restaurants.empty:
        return {"locations": []}
    locs = df_restaurants['location'].dropna().unique().tolist()
    locs = sorted([str(loc).strip() for loc in locs if str(loc).strip()])
    return {"locations": ["Any"] + locs}

@app.post("/api/recommend")
def recommend_restaurants(prefs: UserPreferences):
    if df_restaurants.empty:
        raise HTTPException(status_code=500, detail="Dataset not loaded.")
    if not client:
        raise HTTPException(status_code=500, detail="Groq API key is missing. Check your .env file.")
        
    df = df_restaurants.copy()
    
    if prefs.location:
        loc_term = prefs.location.lower()
        df = df[df['location'].str.lower().str.contains(loc_term, na=False) | 
                df['listed_in(city)'].str.lower().str.contains(loc_term, na=False)]
    if prefs.cuisine:
        cuisine_term = prefs.cuisine.lower()
        df = df[df['cuisines'].str.lower().str.contains(cuisine_term, na=False)]
    if prefs.min_rating:
        df = df[df['clean_rate'] >= prefs.min_rating]
    if prefs.max_budget is not None:
        df = df[df['clean_cost'] <= prefs.max_budget]
            
    df = df.sort_values(by=['clean_rate', 'clean_votes'], ascending=[False, False])
    df = df.drop_duplicates(subset=['name'])
    
    # Get up to 15 matches to show to the user
    top_matches = df.head(15) 
    
    if len(top_matches) == 0:
        return {"recommendations": [], "message": "No restaurants found matching your exact criteria."}
    
    # Prepare MINIMAL JSON structure for Groq to save massive amounts of tokens
    context_data = []
    for _, row in top_matches.iterrows():
        context_data.append({
            "name": str(row['name']),
            "cuisines": str(row['cuisines']),
            "rating": row['clean_rate'] if pd.notnull(row['clean_rate']) else "Unknown"
        })
        
    system_prompt = """
    You are an expert Zomato restaurant recommendation AI. 
    You will receive a list of filtered restaurants and the user's exact preferences.
    Your task is to provide a personalized explanation for ALL the restaurants provided in the list.
    You MUST return ONLY a raw JSON object. Do NOT include markdown blocks like ```json.
    Format your response EXACTLY as this JSON object:
    {
      "recommendations": [
        {
          "restaurant_name": "Name",
          "ai_explanation": "A 1-2 sentence personalized explanation of why this fits the user's specific preferences."
        }
      ]
    }
    """
    
    user_prompt = f"""
    User Preferences:
    - Location: {prefs.location or 'Any'}
    - Max Budget for Two: {prefs.max_budget or 'Any'}
    - Cuisine: {prefs.cuisine or 'Any'}
    - Min Rating: {prefs.min_rating or 'Any'}
    - Additional Preferences: {prefs.additional_preferences or 'None specifically'}
    
    Here is the structured data of restaurants:
    {json.dumps(context_data, indent=2)}
    
    Please return the JSON object with explanations for all restaurants.
    """
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.2, 
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        ai_response_text = response.choices[0].message.content.strip()
        
        if ai_response_text.startswith("```json"):
            ai_response_text = ai_response_text[7:]
        if ai_response_text.endswith("```"):
            ai_response_text = ai_response_text[:-3]
            
        ai_json = json.loads(ai_response_text)
        ai_recs = ai_json.get("recommendations", [])
        
        # Map AI explanations back to the original full dataframe!
        exp_map = {r.get("restaurant_name"): r.get("ai_explanation") for r in ai_recs}
        
        final_results = []
        for _, row in top_matches.iterrows():
            name = str(row['name'])
            final_results.append({
                "restaurant_name": name,
                "cuisine": str(row['cuisines']),
                "rating": row['clean_rate'] if pd.notnull(row['clean_rate']) else None,
                "estimated_cost": str(row['approx_cost(for_two_people)']),
                "url": str(row['url']),
                "ai_explanation": exp_map.get(name, "A great match based on your standard filters.")
            })
            
        return {
            "total_matches_filtered": len(df),
            "recommendations": final_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with AI engine: {str(e)}")
