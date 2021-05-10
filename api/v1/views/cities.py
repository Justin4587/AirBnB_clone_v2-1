#!/usr/bin/python3
"""making cities view"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
import json


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                strict_slashes=False)
def get_la_cities(state_id=None):
    """list of all cities in a state"""
    the_states = storage.all('State').values()
    cities_list = []
    for the_one in the_states:
        if the_one.id == state_id:
            for city in storage.all('City').values():
                if state_id == city.to_dict()['state_id']:
                    cities_list.append(city.to_dict())
            return jsonify(cities_list)
    abort(404)
