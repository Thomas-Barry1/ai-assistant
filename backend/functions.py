from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_response(messages):
    """
    Get a response from the OpenAI API using the provided prompt.
    """
    response = client.responses.create(
        model="gpt-4.1",
        input=messages
    )
    return response.output_text

"""
@ex [{"role": "user", "content": "Hello, how are you?"}]
This is a multi-line 'comment'
using triple quotes (docstring).
It is often used for function documentation.
"""
def send_ai_messages_and_recieve_messages(messages:list):
    resp = get_response(messages)
    messages.append(resp)


