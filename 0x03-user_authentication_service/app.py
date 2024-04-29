#!/usr/bin/env python3
"""
Baic Flask app
"""
from auth import Auth
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)
import bcrypt

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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ Handle login request"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not Auth.valid_login(email, password):
        abort(401)

    session_id = Auth.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id)

    return resp


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Handle logout requests."""
    session_id = request.cookies.get("session_id")
    user = Auth.get_user_from_session_id(session_id)

    if user:
        Auth.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
