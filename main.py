from ollama import chat
from ollama import ChatResponse

# python3 -m venv env
# source env/bin/activate
# pip install ollama

response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
