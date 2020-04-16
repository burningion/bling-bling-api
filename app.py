from flask import Flask
from PIL import Image

import uuid

app = Flask(__name__)

@app.route('/place-bling')
def place_bling():
    return "Image will be here!"

@app.route('/')
def hello_world():
    return 'Hello, World!'
