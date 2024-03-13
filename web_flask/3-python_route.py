#!/usr/bin/python3

""" Starts a Flash Web Application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(c_text):
    """ Prints C followed by the value of text, replacing _ with spaces """
    return 'C ' + c_text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<py_text>', strict_slashes=False)
def pytext(py_text='is cool'):
    """ Display “Python ”, followed by the value of the text variable,
    replacing underscore _ symbols with a space """
    return 'Python ' + py_text.replace('_', ' ')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
