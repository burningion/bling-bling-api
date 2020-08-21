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
        return "You must POST a json Object in the following form: {\"spots\": number, \"image\": \"base64encodedimage\"}"
    else:
        try:
            spot_count = request.json['spots']
            image = request.json['image']
            image_data = re.sub('^data:image/.+;base64', '', image)
        except:
            return "Malformed JSON request! Given: " + str(request.json)

        im = Image.open(BytesIO(base64.b64decode(image_data)))
        paster = Image.open('images/bling.gif')
        im.thumbnail((500, 500))
        width, height = im.size

        bling_width, bling_height = 40, 40

        spots = []
        for i in range(spot_count):
            spots.append((random.randint(0,width - bling_width), random.randint(0,height - bling_height)))
        frames = []
        for frame in ImageSequence.Iterator(paster):
            frame = frame.convert('RGBA')
            frame.thumbnail((bling_width, bling_height))
            curr = im.copy().convert('RGBA')
            for spot in spots:
                curr.paste(frame, spot, mask=frame)
            frames.append(curr)

        buffered = BytesIO()
        frames[0].save(buffered, format="GIF", save_all=True, append_images=frames[1:], loop=0) # save_all necessary for animation
        img_str = base64.b64encode(buffered.getvalue())

        print("Image created!")
        return img_str

@app.route('/')
def hello_world():
    return 'Hello, World!'
