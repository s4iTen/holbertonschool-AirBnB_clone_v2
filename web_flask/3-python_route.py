#!/usr/bin/python3

'''This is the Flask import'''


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """this is the Hello function"""
    return "Hello HBNB!"


@app.route("/hbnb")
def index():
    """this is the index function"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """this function replace '_' with ' ' and concat it with the C char"""
    return "C " + text.replace('_', ' ')


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """this function replace '_' with ' ' and concat it with the C char"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
