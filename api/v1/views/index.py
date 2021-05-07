#!/usr/bin/python3
""" doing things I sort of understand"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def hillbilly():
    return jsonify({"status": "OK"})
