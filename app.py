from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template, request
import os
from askai import question2answer

app = Flask(__name__)

api_key = os.getenv('LLM_API_KEY')
uri = os.getenv('MONGO_URI')


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
mydb = client["data"]
mycol = mydb["FAQ"]


## Add Question and Answer Functionality
# make text field and output Big Enough
# add model and temperature options
# upload Document?
#

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    context = {
        'Question': '',
        'Answer': '42'
    }
    if request.method == 'POST':
        result = request.form.to_dict()
        question = result['QuestionBox']
        answer = question2answer(question)
        # answer = 30
        context = {
            'Question': question,
            'Answer': answer
        }
        x = mycol.insert_one(context)
        # print(x)
    return render_template('hello_world.html', **context)

@app.route('/chart')
def chart():
    return render_template('chart.html')