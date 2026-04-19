# Phase-Wise Architecture: Zomato AI-Powered Restaurant Recommender

This document outlines the strict phase-wise architectural implementation for the AI-powered restaurant recommendation system, adhering to the requirements specified in the `ProblemStatement.md`.

---

## Phase 1: Data Engineering & Ingestion Setup
**Objective:** Acquire, clean, and structure the data to make it easily queryable by the integration layer.

* **Components:**
  * **Data Source Layer:** Hugging Face `datasets` library to pull the `ManikaSaini/zomato-restaurant-recommendation` dataset.
  * **Processing Engine:** Python (`pandas` or `polars`) for data cleaning (handling missing values, normalizing text, standardizing cost and rating columns).
  * **Storage:** 
    * *Option A (In-memory):* Preprocessed CSV/JSON loaded into memory at application startup (suitable for smaller datasets).
    * *Option B (Database):* SQLite or PostgreSQL for structured, fast querying based on user filters.

## Phase 2: Core Backend API & Integration Layer
**Objective:** Build the backend infrastructure that handles user requests, performs initial data filtering, and acts as a bridge to the AI engine.

* **Components:**
  * **Backend Framework:** FastAPI (Python) - highly performant, excellent for AI/Data pipelines, and provides automatic API documentation.
  * **Endpoints:**
    * `POST /api/recommend`: Accepts JSON payload containing user preferences.
  * **Filtering Logic:** 
    * Translates user inputs (e.g., location="Delhi", budget="medium", cuisine="Italian", min_rating=4.0) into database queries or dataframe filters.
    * Limits the filtered results to a manageable subset (e.g., top 10-20 matches) to fit within the LLM context window.

## Phase 3: AI Recommendation Engine (LLM Integration)
**Objective:** Connect the filtered data to a Large Language Model to rank options and generate personalized, human-readable explanations.

* **Components:**
  * **LLM Provider:** Groq API (using models like LLaMA 3). API keys managed via `.env` file.
  * **Prompt Construction Module:**
    * Dynamically builds a prompt combining the user's nuanced preferences (e.g., "family-friendly") with the structured JSON/CSV text of the filtered restaurants.
  * **Structured Output Parsing:**
    * Forces the LLM to return data in a strict JSON format (using function calling or JSON mode) to ensure the frontend can render it deterministically:
      ```json
      [
        {
          "restaurant_name": "...",
          "cuisine": "...",
          "rating": 4.5,
          "estimated_cost": "...",
          "ai_explanation": "..."
        }
      ]
      ```

## Phase 4: Frontend Development (User Input & Display)
**Objective:** Create an intuitive and dynamic user interface for capturing preferences and displaying the AI's recommendations.

* **Components:**
  * **Framework Options:** 
    * *Option A (Rapid Prototyping):* Streamlit (Python) - allows building the UI entirely in Python alongside the backend logic.
    * *Option B (Production Grade):* React (Next.js or Vite) with Tailwind CSS for a highly polished, responsive web application.
  * **User Input Forms:** Dropdowns, sliders, and text inputs for location, budget, cuisines, and custom preferences.
  * **Results UI:** A card-based layout displaying the restaurant details, prominently featuring the `ai_explanation` alongside standard metrics.

## Phase 5: Testing, Refinement, & Deployment
**Objective:** Ensure the system is robust, handles edge cases (like zero matches), and is deployed for access.

* **Components:**
  * **Testing:** 
    * Fallback mechanisms if the LLM API fails.
    * Edge case handling if initial structured filtering yields 0 results (e.g., expanding the search radius or lowering the minimum rating slightly).
  * **Containerization:** Docker for containerizing the backend/frontend services.
  * **Deployment:** Platforms like Render, Vercel (frontend), or Railway for simple, scalable hosting.

---
### System Data Flow Summary
`User UI (Frontend)` ➔ `JSON Request` ➔ `FastAPI Backend` ➔ `Data Filter (Pandas/SQL)` ➔ `Filtered Subset + Prompt` ➔ `LLM API` ➔ `Ranked JSON Results + Explanations` ➔ `FastAPI Backend` ➔ `User UI (Frontend)`
