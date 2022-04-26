#!/usr/bin/env python3.8
import random
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

def main():
    print('Wlecome to your Password Locker')
    print('Select action below to proceed')
    while True:

        print(" 1. LOGIN \n 2. SIGN UP  \n 3. DISPLAY ACCOUNTS \n 4. SIGN OUT")

        selected = int(input())
        if selected == 1:
            print('Enter your account name')
            name_account = input()
            print('Enter your username')
            username = input()
            print('Enter your password')
            password = input()
            account = find_account(name_account)
            if account:

                if account.account == name_account and account.password == password:

                    print('logged in ')
                    while True:

                        print(
                            f'Welcome {username}, select action below using corresponding number')

                        print(
                            ' 1. Save new password \n 2. Delete password \n 3. Display saved password')

                        selectOption = int(input())
                        if selectOption == 1:
                            print('New account')

                            print('account name')
                            account = input()

                            print('1. Create password \n 2.Generate password')
                            choice = int(input())
                            if choice == 1:

                                print('password')
                                password = input()
                            elif choice == 2:
                                randoms = random.randint(1000,9999)
                                print(randoms) 
                                password = randoms

                            else:
                                print('Not an option')      

                            save_accounts(create_account(account, password))

                        elif selectOption == 2:
                            print("Enter the name of the account you want to delete")

                            account = input()
                            if account_exist(account):
                                # remove_account = (account)
                                del_account(account_exist(account))

                            else:
                                print(f'{account} does not exist')

                        elif selectOption == 3:
                            if display_account():
                                for acc in display_account():
                                    print(
                                        f'{acc.account}:{acc.password}'
                                    )
            else:
                print('Does not exist')

        if selected == 2:
            print('Sign Up New acc')

            print('Enter Account Name')
            account_name = input()

            print('Enter Username')
            user_name = input()

            print('Enter Password')
            password = input()

            save_accounts(create_account(
                account_name, password))

            print('Successful')

        elif selected == 3:
            if display_account():
                for account in display_account():
                    print(
                        f'{account.account}'
                    )
            else:
                print('Nothing Yet')

        elif selected == 4:
            print('Thank YOU')
            break


if __name__ == '__main__':
    main()