#!/usr/bin/python3
'''Module to display Python followed by the value text variable
and set the value by default to is cool'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.strip()
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    text = text.strip()
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
