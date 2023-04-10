#!/usr/bin/python3
from flask import Flask
'''This is the Flask import'''


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"
