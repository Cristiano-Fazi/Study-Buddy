from ollama import chat, ChatResponse, create, AsyncClient, pull
import asyncio
import re

# pull("deepseek-r1:7b")
models = ['deepseek-r1:1.5b']
current_chat = chat(models[0], messages=[])
messages = [
    {
      'role': 'user',
      'content': 'You are a teacher and also you are a cat princess and I am so excited to learn from you!'
    }
]

# This function strips the thinking off of the response.
# This can be problematic if the thinking process includes </think> but I believe the model ignores that word and refuses to use it.
def strip_thinking(text):

    index = re.search('</think>', text)
    new_text = text[index.start() + 8:]

    # If we get to the end return text, this should never happen.
    return new_text

def gen_ai_call(subject):
    response = chat(
        models[0],
        messages = messages + 
        [
            {
                'role': 'user', 
                'content': "Please breifly explain the following subject:" + subject
            }
        ],
    )

    to_return = {
        'content' : strip_thinking(response['message']['content']),
    }

    print(to_return['content'])

    return to_return

async def gen_ai_call_async(subject):
    response = await AsyncClient().chat(
        models[0],
        messages = messages + 
        [
            {
                'role': 'user', 
                'content': "Please breifly explain the following subject:" + subject
            }
        ],
    )

    to_return = {
        'content' : strip_thinking(response['message']['content']),
    }

    return to_return

# asyncio.run(gen_ai_call_async('deepseek-r1:7b', ""))



def gen_ai_loop():
    while True:
        # "What would you like to ask the generative AI model? To quit type /quit \n"
        message = input("What would you like to ask the generative AI model? To quit type /quit \n")
        if message == '/quit':
            break
        gen_ai_call(message)

# gen_ai_loop()
