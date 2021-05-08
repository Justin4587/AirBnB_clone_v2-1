#!/usr/bin/python3
""" doing things I sort of understand"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity


@app_views.route('/status', strict_slashes=False)
def hillbilly():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    "Create an endpoint that retrieves the number of each objects by type:"
    count_amenities = storage.count("Amenity")
    count_cities = storage.count("City")
    count_places = storage.count("Place")
    count_reviews = storage.count("Review")
    count_states = storage.count("State")
    count_users = storage.count("User")
    return jsonify(amenities=count_amenities,
                   cities=count_cities,
                   places=count_places,
                   reviews=count_reviews,
                   states=count_states,
                   users=count_users)
