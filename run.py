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

def account_exists(username):
    
    """Function that check if an account exists with that username and return a boolean"""
    return Credential.check_account_exists(username)

def display_credentials():

    """Function that returns all the saved credentials"""
    return Credential.display_credentials()

def create_account(account, password):
    accounts = User(account, password)
    return accounts

def save_accounts(accounts):
    accounts.save_accounts()

def find_account(accounts):
    return User.account_exists(accounts)

def account_exist(accounts):
    return User.account_exists(accounts)

def del_account(accounts):
    accounts.delete_account()

def display_account():
    return User.display_account()

