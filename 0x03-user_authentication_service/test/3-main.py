#!/usr/bin/env python3
""" Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()

email = "techiegold@tech.com"
hashed_password = "MySuperHotPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password="NewSuperHotPwd")
    print("password updated")
except ValueError:
    print("Error")
