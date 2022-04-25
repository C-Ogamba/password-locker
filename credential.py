from requests import delete


class Credential:
    accountlist = []

    def __init__(self, accountname, username, password):
        
        self.accountname = accountname
        self.username = username
        self.password = password
        
    def save_credential(self):
        """saves users credentials """
        Credential.accountlist.append(self)

    def delete_credential(self):
        """deletes users credentials"""
        Credential.accountlist.remove(self)
    
    @classmethod
    def check_account_exists(cls, username):
        """this checks whether the account exists"""
        for account_credentials in cls.accountlist:
            if account_credentials.username == username:
                return True
            # return True if account_credentials.username == username else False
        return False
    @classmethod
    def find_by_username(cls, username):
        """This is to find username credentials by user name"""
        for account_credentials in cls.accountlist:
            if account_credentials.username == username:
                return account_credentials

    @classmethod
    def display_credentials(cls):
        """method that shows the credentials"""
        return cls.accountlist           
        