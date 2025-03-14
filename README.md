## AI Agent Playground  

This project sets up an interactive AI agent playground using OpenAI's GPT models. It includes two agents:  

- **Web Agent**: Uses OpenAI GPT and optionally DuckDuckGo for web searches.  
- **Agent**: A general-purpose AI assistant using OpenAI GPT.  

The agents store conversation history in an SQLite database for contextual awareness.  

---

## Features  

✅ Uses OpenAI GPT models for AI responses  
✅ Supports web search with DuckDuckGo (optional)  
✅ Saves conversation history using SQLite  
✅ Provides a web-based playground UI  

---

## Setup  

### 1. Clone the Repository  
```sh
git clone https://github.com/andrepradika/agno-playground.git
cd agno-playground
```  

### 2. Install Dependencies  
Make sure you have Python installed, then run:  
```sh
pip install -r requirements.txt
```  

### 3. Set Up Environment Variables  
Create a `.env` file in the project root:  
```ini
OPENAI_API_KEY=your_openai_api_key
DUCKDUCKGO_ENABLED=True  # Set to False if not needed
AGENT_STORAGE_PATH=tmp/agents.db  # Change if needed
```  

### 4. Run the Playground  
Start the web-based playground with:  
```sh
python main.py
```  
This launches the app on `http://0.0.0.0:7777`.  

---

## Usage  

- Open your browser and go to `http://localhost:7777`  
- Interact with the AI agents through the web interface  
- The Web Agent can fetch real-time information (if DuckDuckGo is enabled)  

---

## File Overview  

- `main.py`: Entry point for running the app  
- `.env`: Stores API keys and configuration  
- `requirements.txt`: Dependencies required to run the project  
- `tmp/agents.db`: SQLite database storing conversation history  

---

## Contributing  

Feel free to submit issues or pull requests to improve this project.  

---

## License  

This project is licensed under the MIT License.  

---  

## Author  
andrepradika  
---  