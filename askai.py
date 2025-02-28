from openai import OpenAI
import os

api_key = os.getenv("LLM_API_KEY") # Replace with your API key
base_url = "https://chat-ai.academiccloud.de/v1"
model = "meta-llama-3.1-8b-instruct" # Choose any available model

def question2answer(question):

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    # Get response
    chat_completion = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are a helpful assistant"},
                  {"role": "user", "content": question}],
        model=model,
    )

    answer = chat_completion.choices[0].message.content

    return answer