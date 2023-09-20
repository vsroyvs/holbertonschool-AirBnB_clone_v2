#!/usr/bin/python3
""" Module to starts a Flask Web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """ Close the Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_by_states():
    """ List all states on a HTML page """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
