# Zomato AI Recommender

![Zomato UI Showcase](https://img.shields.io/badge/UI-Cyberpunk_Dark_Theme-E23744?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)

An AI-powered restaurant recommendation engine featuring a premium, futuristic dark-mode UI inspired by Zomato. This full-stack application utilizes a FastAPI backend to handle complex filtering logic and integrates an LLM (Groq) for intelligent, context-aware personalized dining suggestions.

## ✨ Features

- **Intelligent Recommendations:** Uses Large Language Models (LLM) to analyze your specific preferences (e.g., "Must have a great view, family-friendly") and provides personalized reasoning for each suggestion.
- **Advanced Filtering:** Filter by Location, Cuisine, Max Budget, and Minimum Rating.
- **Premium UI/UX:** A carefully crafted dark-theme frontend with deep blacks, Zomato's signature red and gold accents, micro-animations, and tactile depth. 
- **High-Performance Backend:** Built with FastAPI for rapid, asynchronous API endpoints.
- **Automated Setup:** Easily spin up both frontend and backend services concurrently with a single script.

## 🛠️ Tech Stack

- **Frontend:** Streamlit, Custom HTML/CSS/JS (Vanilla CSS without Tailwind), Base64 Image Processing
- **Backend:** FastAPI, Python
- **AI / LLM:** Groq API Integration
- **Database:** SQLite (local dataset ingestion)
- **Typography:** DM Sans, Playfair Display, Metropolis

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning)
- An active Groq API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devansh959/Zomato_AI_Recommend.git
   cd Zomato_AI_Recommend
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Ensure you have a `.env` file in the root directory containing your API keys and configuration:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Running the Application

The project includes a convenient batch script to launch both the FastAPI backend and the Streamlit frontend simultaneously.

Simply run:
```bash
.\run_all.bat
```
*(Alternatively, you can run the services manually in separate terminal windows.)*

- The **FastAPI Backend** will run on: `http://localhost:8000`
- The **Streamlit Frontend** will run on: `http://localhost:8501`

To stop the servers, you can run `.\stop_servers.bat` if available, or manually terminate the processes in your terminal (`Ctrl+C`).

## 🎨 Design Philosophy

The frontend was designed with a "Premium Zomato Dark Theme" aesthetic. It explicitly avoids flat SaaS styling in favor of:
- **Layered Surfaces:** Subtle background gradients and glassmorphism.
- **Tactile Depth:** Glow effects (`--shadow-neon`) on active inputs and hover states.
- **Typography:** Serif headings (`Playfair Display`) paired with clean sans-serif body text (`DM Sans` / `Metropolis`).
- **Custom Branding:** Pure CSS Zomato logo injection for high-fidelity rendering.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
