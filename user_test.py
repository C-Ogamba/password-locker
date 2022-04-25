from user import User
import unittest

class Test(unittest.TestCase):

    def tearDown(self):
        User.user_accounts = []

    def setUp(self):

        self.new_password = User("twitter", "123456")

    