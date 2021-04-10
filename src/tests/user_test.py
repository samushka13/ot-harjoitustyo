import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("samushka", "13")

    def test_created_user_exists(self):
        self.assertNotEqual(self.user, None)

    def test_created_username_is_set_correctly(self):
        self.assertEqual(str(self.user.username), "samushka")

    def test_created_password_is_set_correctly(self):
        self.assertEqual(str(self.user.password), "13")
