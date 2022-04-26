from user import User
import unittest

class Test(unittest.TestCase):

    def tearDown(self):
        User.user_accounts = []

    def setUp(self):

        self.new_password = User("twitter", "123456")

    def test_init(self):
        """test to check whether data entered will appear if called"""

        self.assertEqual(self.new_password.account, "twitter")
        self.assertEqual(self.new_password.password, "123456")

    def test_save_account(self):
        """checks whether value is appended to the user' password"""
        self.new_password.save_account()
        self.assertEqual(len(User.user_accounts), 1)

    def test_save_multiple(self):

        self.new_password.save_account()
        test_pass = User("github", "654321")
        test_pass.save_account()
        self.assertEqual(len(User.user_passwords), 2)