#!/usr/bin/env python3
"""
This module contains flask view that handles all routes
for the Session authentication.
"""

from flask import jsonify, request
from models.user import User
from api.v1.views import app_views
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handle user login with session authentication """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    
    if not password:
        return jsonify({"error": "password missing"}), 400
    
    users = User.search({"email": email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 401
    
    from api.v1.app import auth
    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            session_cookie_name = getenv("SESSION_NAME")
            resp = jsonify(user.to_json())
            resp.set_cookie(session_cookie_name, session_id)
            return resp
        
    return jsonify({"error": "wrong password"}), 401
