from flask import Flask, render_template, request, send_from_directory
from mmh3 import hash128
from functions import *
import os

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def colours_post():
    if request.method == 'POST':
        text = request.form['text']
        genType = request.form['palette_type']
        genCheck = request.form.getlist('gen_type')
        hash = hash128(text)
        data = []  

        if genType == 'old':
            data = [text, genRGBlist(hash, len(genCheck))]
        elif genType == 'alt':
            data = [text, genHSLpalette(hash, len(genCheck))]
        return render_template('palette.jinja2', data = data, radio = genType, check = len(genCheck))
    
    else: return render_template('palette.jinja2', data = blankRGB(), radio = 'alt', check = 1)
