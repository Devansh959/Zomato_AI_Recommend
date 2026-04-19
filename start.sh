#!/bin/bash

# Start the FastAPI backend in the background
echo "Starting FastAPI Backend..."
uvicorn src.main:app --host 0.0.0.0 --port 8000 &

# Wait a few seconds for the backend to initialize (especially loading the 574MB DB)
sleep 5

# Start the Streamlit frontend on the port expected by Hugging Face Spaces
echo "Starting Streamlit Frontend..."
streamlit run src/app.py --server.port 7860 --server.address 0.0.0.0
