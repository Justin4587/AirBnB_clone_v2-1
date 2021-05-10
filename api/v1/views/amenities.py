#!/usr/bin/python3
"""making cities view"""
from models.amenity import Amenity
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/amenities/', methods=['GET'],
                 strict_slashes=False)
@app_views.route('/amenities/<amenitiy_id>/', methods=['GET'],
                 strict_slashes=False)
def get_cities_de_amenity(amenity_id=None):
    """list of all cities in a state"""
    the_states = storage.all('Amenity')
    cities_list = []
    if amenity_id is None or amenity_id is "":
        for i in the_states:
            cities_list.append(i.to_dict())
        return jsonify(cities_list)
    for the_one in the_states:
        if the_one.id == amenity_id:
            return jsonify(the_one.to_dict())
        else:
            abort(404)
