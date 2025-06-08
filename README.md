# ChatBor 🧠

A minimal Django chatbot powered by LLaMA 3.2:1B via [Ollama](https://ollama.com).  
Runs locally, no cloud needed.

---

## Features

- Django-powered web chatbot
- Uses LLaMA 3.2:1B model via Ollama
- Local and private AI interactions
- Simple API endpoint for chat

---

## Setup

1. **Clone and enter project:**

```bash
git clone https://github.com/yourusername/chatbor.git
cd chatbor
Create virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate
Install requirements:

bash
Copy
Edit
pip install -r requirements.txt
Install & run Ollama:

bash
Copy
Edit
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3
Run the app:

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Visit http://localhost:8000

API
POST /api/chat/

json
Copy
Edit
{ "message": "Hello" }
Response:

json
Copy
Edit
{ "response": "Hi! How can I help you?" }
License
MIT © 2025

yaml
Copy
Edit

---

Let me know if you want this to include example UI screenshots or Docker support.



