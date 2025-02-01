from ollama import chat
from ollama import ChatResponse
from ollama import create

models = ['deepseek-r1:7b']
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
    key = '</think>'
    variable = ''
    text_index = 0

    # Goes through each character in the text from the start.
    # Variable slowly gains characters so long as they match the key.
    # If variable does not match the key as it is being built then it must mean we are not at </think>
    # If key == variable it means we have found the word </think> and must be at the end of the thinking.
    # Strip all the characters behind that index.
    for char in text:
        variable += char
        if key[:len(variable)] != variable:
            variable = ''
        if key == variable:
            text_index += 1
            return text[text_index:]

    # If we get to the end return text, this should never happen.
    return text

def gen_ai_call(model, text):

    response = chat(
        model,
        messages = messages + 
        [
            {
                'role': 'user', 
                'content': text
            }
        ],
    )

    to_return = {
            'content' : strip_thinking(response['message']['content']),
        }
    

    return to_return

def gen_ai_loop(model):
    while True:
        message = input("What would you like to ask the generative AI model? To quit type /quit \n")
        if message == '/quit':
            break
        gen_ai_call(model, message)

# gen_ai_loop(models[0])
