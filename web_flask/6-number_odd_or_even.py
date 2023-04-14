#!/usr/bin/python3

'''This is the Flask import'''


from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """this function display the n only if it's an integer"""
    return (f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """this function check if the variable is odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, j='is even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, j='is odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
