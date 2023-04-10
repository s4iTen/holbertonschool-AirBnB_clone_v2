#!/usr/bin/python3
from flask import Flask
'''This is the Flask import'''

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """this is the index function"""
    return "Hello HBNB!"

if __name__ == "__main__":
    """this is the """
    app.run()
