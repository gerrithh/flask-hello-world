from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template, request
import os

app = Flask(__name__)

api_key = os.getenv('LLM_API_KEY')
uri = os.getenv('MONGO_URI')


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
mydb = client["data"]
mycol = mydb["FAQ"]


@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    context = {
        'name': 'test',
        'age': '35'
    }
    if request.method == 'POST':
        result = request.form.to_dict()
        context = {
            'name': result['Key'],
            'age': '35'
        }
        mydict = {"name": result['Key'], "address": "Highway 37"}
        x = mycol.insert_one(mydict)
        print(x)
    return render_template('hello_world.html', **context)

@app.route('/chart')
def chart():
    return render_template('chart.html')