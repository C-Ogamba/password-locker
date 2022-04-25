from requests import delete


class User:
    def __init__(self,account,password):
       
        self.name = account
        self.password = password
        
        user_accounts = []

    def delete_account(self):
        """function to delete account"""
       
       
        User.user_accounts.remove(self)

    def save_accounts(self):
        """function to save account"""

        User.user_accounts.append(self)

    @classmethod
    def display_account(cls):
        """method to display all user accounts"""

        return cls.user_accounts

    @classmethod
    def find_by_account(cls, accounts):
        """find account using accountname"""

        for account in cls.user_accounts:
            if account.account == accounts:
                return account

    @classmethod
    def account_exists(cls, accounts):

        for account in cls.user_accounts:
            if account.account == accounts:
                return account
            return False

