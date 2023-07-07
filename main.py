from flask import Flask, render_template, request
from mmh3 import hash128
from functions import *

app = Flask(__name__)

#@app.route("/")
#def colours():
#    return render_template('palette.html', data = blankRGB())

@app.route("/", methods=['GET','POST'])
def colours_post():
    if request.method == 'POST':
        text = request.form['text']
        genType = request.form['palette_type']
        print(genType)
        genCheck = request.form.getlist('gen_type')
        hash = hash128(text)
        data = []  

        if genType == 'old':
            data = [text, genRGBlist(hash, len(genCheck))]
        elif genType == 'alt':
            data = [text, genHSLpalette(hash, len(genCheck))]
        return render_template('palette.html', data = data, radio = genType, check = len(genCheck))
#        elif genType == 'alt:':
#            data = [text, genHSLpalette(hash, len(genCheck))]
#            return render_template('palette.html', data = data, radio = 'new', check = len(genCheck))

#        if genType == 'old': #RGB nonunified
#            data = [text, genRGBlist(hash,0)]
#            return render_template('palette.html', data = data, radio = 'old')
#        elif genType == 'new': # RGB unified
#            data = [text, genRGBlist(hash,1)]
#            return render_template('palette.html', data = data, radio = 'new')
#        elif genType == 'alt':
#            data = [text, genHSLpalette(hash,0)]
#            return render_template('palette.html', data = data, radio = 'alt')
    else: return render_template('palette.html', data = blankRGB(), radio = 'old', check = 1)