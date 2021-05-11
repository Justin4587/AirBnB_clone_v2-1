#!/usr/bin/python3
"""making cities view"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
import json


@app_views.route('/places/<place_id>/reviews',
                 methods=["GET"], strict_slashes=False)
def review_place(place_id=None):
    """review plcase"""
    the_reviews = storage.all('State').values()
    review_list = []
    for the_one in the_reviews:
        if the_one.id == place_id:
            review_list.append(value.to_dict())
        return (jsonify(review_list))
    abort(404)
