from ollama import chat
from ollama import ChatResponse

def gen_ai_call(model, text):
    response: ChatResponse = chat(model, messages=[
    {
        'role': 'user',
        'content': text,
        'stream': True
    }
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    # print(response.message.content)

def gen_ai_loop():
    while True:
        message = input("What would you like to ask the generative AI model? To quit type /quit \n")
        if message == '/quit':
            break
        gen_ai_call("deepseek-r1:7b", message)

#gen_ai_call("deepseek-r1:7b", "How many people are there on Earth?")