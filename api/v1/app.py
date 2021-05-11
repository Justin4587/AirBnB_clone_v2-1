#!/usr/bin/python3
""" making an app i am making an app todaaay"""
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from models import storage
import os
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins='0.0.0.0')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown_api(exception):
    """ tearing down things """
    return storage.close()


@app.errorhandler(404)
def err_handle(error):
    """ stuff about errors is here"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if host is None:
        host = "0.0.0.0"
    if port is None:
        port = "5000"
    app.run(host=host, port=port, threaded=True)
