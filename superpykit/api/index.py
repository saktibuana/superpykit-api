from flask import Flask
import inlinetohandwriting

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/tulisantangan/<tulisan>/<warna>')
def tulisantangan(tulisan=None, warna=None):

    return tulisan + " " + warna