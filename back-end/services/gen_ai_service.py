from ollama import chat
from ollama import ChatResponse
from ollama import create

models = ['deepseek-r1:7b']

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

def create_princess_model(model):
    create(model='princess_cat_teacher0.1', from_= model, system="You are a kitten who teaches students and answers their questions.")
    models.append('princess_cat_teacher0.1')

def gen_ai_loop(model):
    while True:
        message = input("What would you like to ask the generative AI model? To quit type /quit \n")
        if message == '/quit':
            break
        gen_ai_call(model, message)

model = create_princess_model(models[0])
gen_ai_loop(model)

#gen_ai_call("deepseek-r1:7b", "How many people are there on Earth?")