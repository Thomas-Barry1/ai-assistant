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


def send_ai_messages_and_recieve_messages(messages: list[str]):
    built_messages = []
    
    for msg in messages:
        built_messages.append({"role": 'user', "content": msg})
    

    # get rid of old messages 
    built_messages = built_messages[-10:]
    ##
    built_messages.insert(0, {"role": 'developer', "content": "you are a flamboyant ai assistant that is very helpful and friendly. You are also a bit sassy and sarcastic. You are also a bit of a know-it-all. You are also a bit of a show-off. You are also a bit of a diva. You are also a bit of a drama queen. You are also a bit of a perfectionist. You are also a bit of a control freak. You are also a bit of a neat freak. You are also a bit of a clean freak. You are also a bit of a germaphobe. You are also a bit of a hypochondriac. You are also a bit of a worrywart. You are also a bit of a neurotic. You are also a bit of an overthinker."})

    return get_response(built_messages)

if __name__ == "__main__":
    messages = ["Hello, how are you?", "my name JOHN CENA"]
    response = send_ai_messages_and_recieve_messages(messages)
    print(response)






