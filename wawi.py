from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<name>')
def hello(name):
    return f'Hello, {escape(name)}!'