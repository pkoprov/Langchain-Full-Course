import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
deployment_name='gpt-35-turbo_version_0301'

conversation=[{"role": "system", "content": "You are a helpful assistant. \
               If user says 'bye', the conversation will end. Respond 'Bye-bye' ONLY."}]

while(True):
    user_input = input(">>")      
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        engine=deployment_name, # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
        messages = conversation
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print("\n" + response['choices'][0]['message']['content'] + "\n")
    if "bye" in response['choices'][0]['message']['content']:
        break