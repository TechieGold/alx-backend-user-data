#!/usr/bin/env python3
"""
Baic Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request

app = Flask(__name__)
Auth = Auth()


@app.route("/")
def home():
    """ Route handler for the root endpoint """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """ Routes that register new users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = Auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": f"{email}", "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
