from flask import Flask
import sebaristulisantangan

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/tulisantangan/<tulisan>/<warna>')
def tulisantangan(tulisan=None, warna=None):
    # inlinetohandwriting(tulisan)
    return tulisan + " " + warna