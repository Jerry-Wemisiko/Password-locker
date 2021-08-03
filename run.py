#!/usr/bin/env python3
from passwd import User
from passwd import Credential

def create_password(user_name,password):

    new_user = User(user_name,password)
    return new_user

def save_user(user):
    
    user.save_user()

def delete_user(user):

    user.delete_user()


