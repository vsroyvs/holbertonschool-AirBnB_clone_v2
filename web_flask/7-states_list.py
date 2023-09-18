#!/usr/bin/python3
'''Module to starts a Flask Web application,
and to display all State objects'''
from flask import Flask, render_template
from models import storage
from models.states import State


app = Flask(__name__)


@app.teardown_appcontext
def close(Exception):
    """Close the Session"""
    storage.close()


@app.route('states_list', strict_slashes=True)
def states_list():
    """List all states on a HTML page"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html',states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
