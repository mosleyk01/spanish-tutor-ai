# spanish-tutor-ai
Spanish Tutor AI is a web-based conversational language learning tool designed to help users practice Spanish in a friendly, supportive environment. It adapts its teaching approach based on the user's proficiency level — beginner, intermediate, or advanced — using a locally hosted AI model (e.g., LLaMA 3.2 via Ollama). The app aims to improve fluency through realistic, low-pressure chat interactions.

## Features

- Web interface using HTML/CSS/JavaScript  
- AI conversation engine using Flask (Python backend)  
- System prompt adapts to three levels: beginner, intermediate, advanced  
- Text-to-speech integration for AI responses  
- Conversation state management and resetting  
- Runs offline with no external API calls (uses Ollama locally)

## Technologies Used

- Python (Flask)  
- HTML/CSS/JavaScript  
- Ollama (LLaMA 3.2 model)  
- Web Speech API (Text-to-Speech)

## Getting Started

### Prerequisites

- Python 3.x  
- Ollama installed locally with the LLaMA 3.2 model downloaded  
- Flask (`pip install flask`)

### Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/mosleyk01/spanish-tutor-ai.git
   cd spanish-tutor-ai
   ```

2. Start Ollama locally (ensure the model name in `ai_chat.py` matches your installed one):
   ```bash
   ollama run llama3.2
   ```

3. Run the Flask server:
   ```bash
   python main.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

## File Structure

```text
.
├── ai_chat.py        # Core conversation logic with user-level-specific prompts
├── main.py           # Flask app managing routes and API
├── index.html        # Frontend UI
├── script.js         # Chat interaction + speech synthesis
├── style.css         # Basic styling
```

## Example Use

- Choose your Spanish level (e.g., beginner)  
- Type a message (e.g., “Hola, ¿cómo estás?”)  
- Receive supportive and level-appropriate feedback  
- Listen to the response using built-in speech synthesis
