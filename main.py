from ollama import chat
from ollama import ChatResponse

# Run this in command prompt
# python -m venv env
# env\Scripts\activate
# pip install ollama

# python3 main.py

response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
