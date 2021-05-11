#!/usr/bin/python3
"""making cities view"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User
import json


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id=None):
    """list of all users"""
    the_users = storage.all('user').values()
    users_list = []
    for the_one in the_users:
        if the_one.id == user_id:
            return jsonify(the_one.to_dict())
    abort(404)

