#!/usr/bin/env python3.8
from user import User
from credential  import Credential

def create_credential(accountname, username,password):
    """Function to create a new credential"""
    credential = Credential(accountname, username, password)
    return credential

def save_credential(credential):
    """Function to save credential"""
    credential.save_credential()

def del_credential(credential):
    """Function to delete a credential"""
    credential.delete_credential()

def find_account(username):
    """Function that finds an account by username and return the contact"""
    return Credential.find_by_username(username)

