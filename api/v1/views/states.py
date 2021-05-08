#!/usr/bin/python3
""" making states i am making states with corbin """
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
import json

    
@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_a_state(state_id=None):
    """ get stuff """
    the_states = storage.all('State').values()
    state_list =[]
    if state_id is None or state_id is "":
        for i in the_states:
            state_list.append(i.to_dict())
        return jsonify(state_list)
    for the_one in the_states:
        if the_one.id == state_id:
            return jsonify(the_one.to_dict())
        else:
            abort(404)

@app_views.route('/states/<state_id>', methods=['DELETE'],
                strict_slashes=False)
def delete_state(state_id=None):
    """Delete a state"""
    the_states = storage.all('State').values()
    for the_one in the_states:
        if the_one.id == state_id:
            the_one.delete()
            storage.save()
            return {}
    abort(404)
