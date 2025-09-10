# Agentic Challenge

Welcome!  
This project contains two parts:  
- **Level 1:** Scripts for AI chat and PDF reading.
- **Level 2:** Weather agent and client using FastMCP.

---

## Folder Structure

agentic-challenge/
level1/
llm_call.py # Gemini AI Q&A
pdf_chat.py # Chat with your PDF
pdf_reader.py # Basic PDF reader
sample.pdf # Example PDF
level2/
weather_mcp.py # Weather info server
client_agent.py # Client to get weather
requirements.txt # All needed Python packages
README.md # This guide!

---

## How to Use

### 1. Install Packages

Open terminal in your main folder and run:
pip install -r requirements.txt


### 2. Run Level 1 Scripts

- For Gemini Q&A:
python level1/llm_call.py

- For PDF chat:
streamlit run level1/pdf_chat.py

### 3. Run Level 2 Weather Agent

- Start the server:
python level2/weather_mcp.py

- Run the client:
python level2/client_agent.py

- Ask it about city weather (needs a free OpenWeatherMap API key).

---

## Notes

- You may need to set up your API keys for Google Gemini and OpenWeatherMap in the relevant scripts.
- All code is beginner-friendly and well-commented.

---
