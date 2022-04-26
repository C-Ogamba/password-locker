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
        self.new_password.save_accounts()
        self.assertEqual(len(User.user_accounts), 1)

    def test_save_multiple(self):

        self.new_password.save_accounts()
        test_pass = User("github", "654321")
        test_pass.save_accounts()
        self.assertEqual(len(User.user_accounts), 2)

    def test_delete_account(self):
        """check whether the delete function removes accounts"""

        self.new_password.save_accounts()
        test_pass = User("github", "654321")
        test_pass.save_accounts()
        self.assertEqual(len(User.user_accounts), 1)

    def test_display_account(self):
        self.assertEqual(User.display_account(), User.user_accounts)

    def test_find_account(self):
        """test checks whether account password is saved"""
        self.new_password.save_accounts()
        test_pass = User("github", "654321")
        test_pass.save_accounts()
        found_account =User.find_by_account("github")
        self.assertEqual(found_account.account, test_pass.account)

    def account_exits(self):


if __name__ == '__main__':
    unittest.main()   