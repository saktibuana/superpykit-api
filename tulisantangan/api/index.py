from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/tulisantangan')
def tulisantangan(tulisan, warna):
    return tulisan + " " + warna