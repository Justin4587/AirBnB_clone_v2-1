#!/usr/bin/python3
"""making cities view"""
from models.amenity import Amenity
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
import json



@app_views.route('/amenities/', methods=['GET'],
                 strict_slashes=False)
@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_cities_de_amenity(amenity_id=None):
    """list of all cities in a state"""
    the_amenities = storage.all('Amenity').values()
    cities_list = []
    if amenity_id is None or amenity_id is "":
        for i in the_amenities:
            cities_list.append(i.to_dict())
        return jsonify(cities_list)
    for the_one in the_amenities:
        if the_one.id == amenity_id:
            return jsonify(the_one.to_dict())
        else:
            abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id=None):
    """Delete a state"""
    the_states = storage.all('Amenity').values()
    for the_one in the_states:
        if the_one.id == amenity_id:
            the_one.delete()
            storage.save()
            return {}
    abort(404)


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def create_a_amenity():
    """create a state"""
    the_state = request.get_json()
    if not the_state:
        abort(400, {'Not a JSON'})
    elif 'name' not in the_state:
        abort(400, {'Missing name'})
    my_state = Amenity(**the_state)
    storage.new(my_state)
    storage.save()
    return jsonify(my_state.to_dict(), 201)
