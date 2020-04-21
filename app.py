from flask import Flask, request
from PIL import Image
from io import BytesIO

import base64
import uuid
import re

app = Flask(__name__)

@app.route('/place-bling', methods=['GET', 'POST'])
def place_bling():
    if request.method == 'GET':
        return "You must POST a json Object in the following form: {\"image\": \"base64encodedimage\"}"
    else:
        try:
            image = request.json['image']
            image_data = re.sub('^data:image/.+;base64', '', image)
            im = Image.open(BytesIO(base64.b64decode(image_data)))
            im.save('test.gif', save_all=True) # save_all necessary for animation
            return "Image created!"
        except:
            return "Malformed image request!"

@app.route('/')
def hello_world():
    return 'Hello, World!'
