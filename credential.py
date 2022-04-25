from requests import delete


class Credential:
    passwords = []

    def __init__(self, accountname, username, password):
        
        self.accountname = accountname
        self.username = username
        self.password = password
        
    def save_user_credentials(self):
        """saves users credentials """
        Credential.passwords.append(self)

    def delete_user_credentials(self):
        """deletes users credentials"""
        Credential.passwords.remove(self)
    
    @classmethod
    def check_account_exists(cls, accountname):
        """this checks whether the account exists"""
        for account_credentials in cls.passwords:
            return True if account_credentials.accountname == accountname else False

    @classmethod
    def find_user_name_credentials(cls, accountname):
        """This is to find accountname credentials by user name"""
        for account_credentials in cls.passwords:
            if account_credentials.accountname == accountname:
                return account_credentials

    @classmethod
    def display_credentials(cls):
        """method that shows the credentials"""
        return cls.passwords           
        