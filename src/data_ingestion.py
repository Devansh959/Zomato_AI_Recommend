import os
import sqlite3
import pandas as pd
from datasets import load_dataset

def main():
    print("Loading Zomato dataset from Hugging Face...")
    # Load dataset from Hugging Face
    dataset = load_dataset('ManikaSaini/zomato-restaurant-recommendation')
    
    print("Converting to Pandas DataFrame...")
    # Typically train split contains the data
    df = dataset['train'].to_pandas()
    
    print(f"Dataset shape before cleaning: {df.shape}")
    
    # Clean column names (replace spaces with underscores, lowercase)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    
    # Fill missing values if necessary
    # Example: df.fillna("Unknown", inplace=True)
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    db_path = 'data/zomato.sqlite'
    
    print(f"Saving to SQLite database at {db_path}...")
    # Save to SQLite
    with sqlite3.connect(db_path) as conn:
        df.to_sql('restaurants', conn, if_exists='replace', index=False)
        
    print("Data ingestion complete!")
    print(f"Total records saved: {len(df)}")
    
if __name__ == "__main__":
    main()
