from flask import Flask, request
from PIL import Image

import uuid

app = Flask(__name__)

@app.route('/place-bling', methods=['GET', 'POST'])
def place_bling():
    if request.method == 'GET':
        return "You must POST a json Object in the following form: {\"image\": \"base64encodedimage\"}"
    else:
        return "Image will be here!"

@app.route('/')
def hello_world():
    return 'Hello, World!'
