#!/usr/bin/env python3
from passwd import User
from passwd import Credential
def create_new_user(user_name,password):

    new_user = User(user_name,password)
    return new_user

def save_user(user):

    user.save_user()

def delete_user(user):

    user.delete_user()

def display_user():

    return User.display_user()

def login_user(username,password):

    confirm_user = Credential.assert_user(username,password)
    return confirm_user

def create_new_credential(site,username,password):

    new_credential =Credential(site,username,password)
    return new_credential

def save_credential(credentials):

    credentials.save_credentials()

def delete_credential(credentials):

    credentials.delete_credential()

def find_by_username(username):

    return Credential.find_by_username(username)

def generate_password():

    gen_passwd= Credential.generate_password()
    return gen_passwd

def main():
    print("Welcome to Password locker,what is your name?")
    user_name = input()







