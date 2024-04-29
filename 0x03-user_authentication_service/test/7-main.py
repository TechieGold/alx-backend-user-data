#!/usr/bin/env python3
"""
Main
"""
from auth import Auth

email = "gold@tech.com"
password = "MySuperPwd"
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("fake@gmail.com"))
