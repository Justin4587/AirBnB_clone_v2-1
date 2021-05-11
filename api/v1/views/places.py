#!/usr/bin/python3
"""making cities view"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_cities_de_places(city_id=None):
    """list of all cities in a state"""
    the_cities = storage.all('City').values()
    the_places = storage.all('Place').values()
    cities_places = []
    for the_one in the_cities:
        if the_one.id == city_id:
            for the_one_place in the_places:
                if the_one_place.city_id == city_id:
                    cities_places.append(the_one_place.to_dict())
            return jsonify(cities_places)
    abort(404)
