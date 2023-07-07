from flask import Flask, render_template, request
#from markupsafe import escape
from mmh3 import hash128
import random
from scipy.spatial import distance
import numpy as np

app = Flask(__name__)

#@app.route("/")
#def colours():
#    return render_template('palette.html', data = blankRGB())

@app.route("/", methods=['GET','POST'])
def colours_post():
    if request.method == 'POST':
        text = request.form['text']
        genType = request.form['palette_type']
        hash = hash128(text)
        if genType == 'old':
            data = [text, genRGBlist(hash,0)]
            return render_template('palette.html', data = data, radio = 'old')
        elif genType == 'new':
            data = [text, genRGBlist(hash,1)]
            return render_template('palette.html', data = data, radio = 'new')
    else: return render_template('palette.html', data = blankRGB(), radio = 'old')

#@app.route("/<text>")
#def palette(text):
#    hash = hash128(text)
#    data = [text, genRGBlist(hash)]
#    #print(data)
#    return render_template('palette.html', data = data)
#    #return f'colour palette for {escape(text)}'

def genRGB():
    return([random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])

def genRGBlist(seed,version):
    random.seed(seed)
    temp = []
    for n in range(16):
        rgb = (genRGB())
        temp.append(rgb)
    #    temp.append(rgbToHex(rgb[0],rgb[1],rgb[2]))
    temp = rgbNN(temp)
    if version == 1:
        temp = newGen(temp)
    for n in range(len(temp)):
        temp[n] = rgbToHex(temp[n][0],temp[n][1],temp[n][2])
    return temp

def blankRGB():
    temp=[]
    for n in range(16):
        temp.append('#FFFFFF')
    return [False, temp]

def rgbToHex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def NN(A, start):
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which 
                                   # locations have not been visited
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmin(A[last][mask]) # find minimum of remaining locations
        next_loc = np.arange(N)[mask][next_ind] # convert to original location
        path.append(next_loc)
        mask[next_loc] = False
        cost += A[last, next_loc]

    return path, cost

def rgbNN(rgbValues):
    array = np.zeros([16,16])
    for x in range(0, 15):
        for y in range(0, 15):
            array[x,y] = distance.euclidean(rgbValues[x],rgbValues[y])
    
    path, _ = NN(array, 0)

    colours_nn = []
    for i in path:
        colours_nn.append(rgbValues[i])

    return colours_nn

def newGen(rgbValues):
    baseColours = random.randrange(2,5)
    print(baseColours)
    newValues = rgbValues
    keep = []
    split = []
    match baseColours:
        case 2:
            keep = [0,15]
            split = [0,random.randrange(3,12)]
        case 3:
            keep = [0,8,15]
            split = [0,random.randrange(2,6),random.randrange(10,13)]
        case 4:
            keep = [0,5,10,15]
            split = [0,random.randrange(2,3),random.randrange(7,8),random.randrange(12,13)]

    for n in range(0,len(rgbValues)-1):
        if n in split:
            newValues[n] = rgbValues[keep[split.index(n)]]
        else: newValues[n] = jitterRGB(newValues[n-1])

    newValues = rgbNN(newValues)
    return(newValues)


def jitterRGB(rgb):
    return [jitterChannel(rgb[0]),jitterChannel(rgb[1]),jitterChannel(rgb[2])]
    
def jitterChannel(colourChannel):
    upDown = random.randrange(0,1)
    delta = random.randrange(0,100)
    new = 127
    match upDown:
        case 0: new = colourChannel - delta
        case 1: new = colourChannel + delta
    if new > 255: return 255 - delta
    elif new < 0: return 0 + delta
    else: return new
