#!/usr/bin/python3
"""
index
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """return status in json format"""
    s = {"status": "OK"}
    return jsonify(s)

@app_views.route('/stats')
def stats():
    classes = [("amenities", "Amenity"), ("cities", "City"),
               ("places", "Place"), ("reviews", "Review"),
               ("states", "State"), ("users", "User")]
    retval = {key: storage.count(val) for key, val in classes}
    return jsonify(retval)
