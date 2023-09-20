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


@app.route('/states', strict_slashes=False)
def states():
    """ List all states on a HTML page """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """ List all states on a HTML page """
    states = storage.all(State).get(f'State.{id}')
    cities = storage.all(City).values()
    return render_template('9-states.html', states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
