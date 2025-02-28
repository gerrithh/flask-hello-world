from flask import Flask
import os
app = Flask(__name__)

api_key = os.getenv('LLM_API_KEY')
# print(api_key)
@app.route('/')
def hello_world():
    return f'Hello, World!..,{api_key}'
