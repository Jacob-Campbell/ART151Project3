from flask import Flask, render_template, request, jsonify, redirect
import time
from random import randint
import requests

app = Flask(__name__)

# In order to run program open this directory in the terminal and execute this command 'python.exe app.py' then click on the last link found in the terminal

@app.route('/', methods = ['GET', 'POST'])

#define index function

def index():
    catcall = requests.get('https://aws.random.cat/meow')
    catlink = catcall.json()["file"]

    catcall2 = requests.get('https://aws.random.cat/meow')
    catlink2 = catcall2.json()["file"]

    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)