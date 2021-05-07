#!/usr/bin/python3
""" making states i am making states with corbin """
from flask import Flask, jsonify, abort
from api.v1.views import app_views
from models import storage
import models


@app_views.route('/states', strict_slashes=False)
def get_states():
    """ get states """
    the_states = storage.all(State).values()
    state_list =[]
    for i in the_states:
        state_list.append(i.to_dict())
    return jsonify(state_list)
    
