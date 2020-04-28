from flask import Flask, request
from PIL import Image, ImageSequence
from io import BytesIO

import base64
import uuid
import re

import random

app = Flask(__name__)

@app.route('/place-bling', methods=['GET', 'POST'])
def place_bling():
    if request.method == 'GET':
        return "You must POST a json Object in the following form: {\"image\": \"base64encodedimage\"}"
    else:
        try:
            image = request.json['image']
            spot_count = request.json['spots']

            image_data = re.sub('^data:image/.+;base64', '', image)
            im = Image.open(BytesIO(base64.b64decode(image_data)))
            paster = Image.open('images/bling.gif')
            im.thumbnail((500, 500))
            spots = []
            for i in range(spot_count):
                spots.append((random.randint(0,500), random.randint(0,500)))
                frames = []
            for frame in ImageSequence.Iterator(paster):
                frame = frame.convert('RGBA')
                frame.thumbnail((40, 40))
                curr = im.copy().convert('RGBA')
                for spot in spots:
                    curr.paste(frame, spot, mask=frame)
                frames.append(curr)
            frames[0].save('images/test.gif', save_all=True, append_images=frames[1:], loop=0) # save_all necessary for animation
            return "Image created!"
        except:
            return "Malformed JSON request!"

@app.route('/')
def hello_world():
    return 'Hello, World!'
