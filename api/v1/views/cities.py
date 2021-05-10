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
def get_cities_de_state(state_id=None):
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

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id=None):
    """get city"""
    the_cities = storage.all('City').values()
    for the_one in the_cities:
        if the_one.id == city_id:
            return jsonify(the_one.to_dict())
    abort(404)

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id=None):
    """nuke city"""
    the_cities = storage.all('City').values()
    for the_one in the_cities:
        if the_one.id == city_id:
            the_one.delete()
            storage.save()
            return {}
    abort(404)
