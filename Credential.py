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
    
    