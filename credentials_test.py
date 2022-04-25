import unittest
from credential import Credential

class TestCredentials(unittest.TestCase):

    def setUp(self):
        """setup method which will run before each test case"""
        self.platform = Credential("github", "cindy", "123456")
        Credential.passwords = []

    def test_init(self):
        '''
        test_init test case for testing
        '''
        self.assertEqual(self.new_credential.accountname, "github")
        self.assertEqual(self.new_credential.username, "cindy")
        self.assertEqual(self.new_credential.password, "123456")

    def test_save_credential(self):
        """tests credentials save method if it appends to array"""
        self.assertEqual(len(Credential.passwords), 0)
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.passwords), 1)

    def tearDown(self):

        Credential.passwords = []

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "telegram", "mary", "989898")  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.passwords), 2)

    def test_delete_platform_credentials(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.passwords), 1)
        test_credential = Credential("twitter", "candy", "713288")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.passwords), 0)

    def test_find_by_user_name(self):
        '''
        test to check if we can find a user details by username and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("twitter", "candy", "713288")
        test_credential.save_credential()

        found_credential = Credential.find_by_username("candy")

        self.assertEqual(found_credential.username, test_credential.username)
    
    def test_account_exists(self):
        """test if the platform_exists method returns the correct value"""
        self.new_credential.save_credential()
        test_credential = Credential("twitter", "candy", "713288")
        test_credential.save_credential()

        credential_exists = Credential.account_exists("candy")

        self.assertTrue(credential_exists)

    def test_display_the_credentials(self):
        """test to see if it returns all the saved credentials"""
        self.new_credential.save_credential()

        self.assertEqual(Credential.display_the_credentials(), Credential.passwords)

if __name__ == "__main__":
    unittest.main()
    