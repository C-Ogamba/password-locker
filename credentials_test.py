import unittest
from Credential import Credential

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