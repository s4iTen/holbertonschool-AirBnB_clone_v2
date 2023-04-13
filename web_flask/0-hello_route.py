#!/usr/bin/python3
from flask import Flask
'''This is the Flask import'''

app = Flask(__name__)


if __name__ == "__main__":
    """this is the """
    app.run(host='0.0.0.0', port=5000)

    @app.route('/', strict_slashes=False)
    def Hello():
        """this is the index function"""
        return "Hello HBNB!"
