# chat/langchain_bot.py

from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

template = """
You are a helpful AI chatbot. Respond conversationally.

Chat history:
{context}

User: {question}
AI:
"""

# Initialize the prompt
prompt = ChatPromptTemplate.from_template(template)

# Initialize the Ollama model
model = OllamaLLM(model="llama3.2:1b")  # Make sure this model name matches your local ollama model

# Compose the chain (prompt -> model)
chain = prompt | model

chat_history_context = ""

def ask_bot(question):
    global chat_history_context
    response = chain.invoke({
        "context": chat_history_context,
        "question": question
    })
    chat_history_context += f"\nUser: {question}\nAI: {response}"
    return response
