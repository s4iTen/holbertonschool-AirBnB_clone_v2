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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
