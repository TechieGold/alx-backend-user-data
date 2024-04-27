#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = "gold@tech.com"
password = "MySecurePwd"
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, password="WrongPwd"))

print(auth.valid_login("unknown@user.com", password))
