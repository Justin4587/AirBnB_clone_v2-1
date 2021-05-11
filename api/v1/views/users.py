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
    if user_id is None:
        users = [user.to_dict() for user in storage.all("User").values()]
        return jsonify(users)
    the_users = storage.all('User').values()
    for the_one in the_users:
        if the_one.id == user_id:
            return jsonify(the_one.to_dict())
        else:
            abort(404)

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id=None):
    """delete user"""
    the_users = storage.all('User').values()
    for the_one in the_users:
        if the_one.id == user_id:
            the_one.delete()
            storage.save()
            return {}
    abort(404)

