import unittest
from repositories.database_services import DatabaseServices
from services.login_services import LoginServices
from entities.user import User
from config import TEST_DATABASE_FILENAME

class TestLoginServices(unittest.TestCase):
    def setUp(self):
        self.window = None
        DatabaseServices(TEST_DATABASE_FILENAME).database.execute("DROP TABLE IF EXISTS Users")
        self.database = DatabaseServices(TEST_DATABASE_FILENAME)
        self.service = LoginServices(self.window, self.database)
        self.user = User("samushka", "13")
        self.database.add_user(self.user)
        self.user_invalid = User("s", "")
        self.user_not_exists = User("sam", "")
        self.user_input_invalid = User("samushka", "")
        self.all_users = self.database.get_users()

    def test_check_username_length(self):
        self.assertEqual(
            self.service.check_username_length(self.user_invalid.username), False)
        self.assertEqual(self.service.check_username_length(self.user.username), True)

    def test_check_username_and_password(self):
        self.assertEqual(
            self.service.check_username_and_password(
                self.user.username, self.user.password), True)
        self.assertEqual(
            self.service.check_username_and_password(
                self.user_input_invalid.username, self.user_input_invalid.password), False)

    def test_check_credentials_not_matching(self):
        self.assertEqual(
            self.service.check_credentials_not_matching(self.user.username), True)
        self.assertEqual(
            self.service.check_credentials_not_matching(self.user_not_exists.username), False)

    def test_register_new_user(self):
        self.assertEqual(
            self.service.register_new_user(
                self.user.username, self.user.password), (self.user.username, self.user.password))

    def test_check_registration_success(self):
        self.assertEqual(self.service.check_registration_success(self.user.username), True)
        self.assertEqual(self.service.check_registration_success(self.user_invalid.username), False)

    def test_check_for_users(self):
        if self.all_users == 0:
            self.assertEqual(self.service.check_for_users(), False)
        else:
            self.assertEqual(self.service.check_for_users(), True)

    def test_list_all_users(self):
        self.database.add_user(User("another", ""))
        self.all_users = self.database.get_users()
        if self.all_users == 0:
            self.assertEqual(self.service.list_all_users(), None)
        else:
            self.assertEqual(self.service.list_all_users(), '\n'.join(sorted(self.all_users)))

    def test_handle_login(self):
        self.assertEqual(len(self.database.get_logged_in_users()), 0)
        self.service.handle_login(self.user.username)
        self.assertEqual(len(self.database.get_logged_in_users()), 1)
