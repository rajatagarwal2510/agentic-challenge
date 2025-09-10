# Agentic Challenge

A simple project with two levels:  
- **Level 1:** AI and PDF tools  
- **Level 2:** Weather agent (server & client)

---



## Setup Steps

### Install Project Dependencies

Clone this repository: git clone https://github.com/rajatagarwal2510/agentic-challenge.git

navigate to folder: cd agentic-challenge

Then install requirements:
pip install -r requirements.txt

---

## Running Level 1 Tools

### Gemini Q&A

Run in terminal:
python level1/llm_call.py


### PDF Chat (Streamlit Web App)

Run in terminal:
streamlit run level1/pdf_chat.py

This opens a web app to chat with a PDF.  
Upload your own document or use `sample.pdf`.

### PDF Reader

Run in terminal:
python level1/pdf_reader.py

Reads and prints contents of `sample.pdf`.

---

## Running Level 2 Tools

### 1. Start Weather MCP Server

Run in terminal:
python level2/weather_mcp.py

This starts an MCP server for weather queries at port 8080.  
You need an **OpenWeatherMap API key** inside `weather_mcp.py` (`API_KEY = "your_key_here"`).

### 2. Run Weather Client Agent

Open new terminal and run:
python level2/client_agent.py

Type questions like:
- `Weather in Delhi`
- `Temperature of Mumbai`

The client extracts the city and gets live weather info.

---



