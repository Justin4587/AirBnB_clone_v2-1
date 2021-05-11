#!/usr/bin/python3
"""making cities view"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User
import json


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_a_user(user_id=None):
    """ get stuff """
    the_users = storage.all('User').values()
    user_list = []
    if user_id is None or user_id is "":
        for i in the_users:
            state_list.append(i.to_dict())
        return jsonify(user_list)
    for the_one in the_users:
        if the_one.id == user_id:
            return jsonify(the_one.to_dict())
        else:
            abort(404)
