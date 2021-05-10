import unittest
from config import TEST_DATABASE_FILENAME as test_database
from repositories.database_services import DatabaseServices
from services.settings_services import SettingsServices
from entities.user import User
from entities.question import Question
from ui.widgets import combobox


class TestSettingsServices(unittest.TestCase):
    def setUp(self):
        # ---------------------------------------------------------------------
        # First the test database is cleared just to be sure it's empty.
        # ---------------------------------------------------------------------
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Users")
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Questions")
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Games")
        # ---------------------------------------------------------------------
        # Then the services and test database are initialized.
        # ---------------------------------------------------------------------
        self.database = DatabaseServices(test_database)
        self.service = SettingsServices(self.database)
        # ---------------------------------------------------------------------
        # Finally, entities and attributes are initialized to ease testing.
        # ---------------------------------------------------------------------
        self.user = User("samushka", "13", 1)
        self.database.add_user(self.user.username, self.user.password)
        self.database.add_logged_in_user(self.user.username)
        self.question = Question(1, "Category", "Difficulty", "Question?", "Answer!")
        self.database.save_question_item(
            1,
            self.question.category,
            self.question.difficulty,
            self.question.question,
            self.question.answer,
        )

    def test_get_default_players(self):
        self.assertEqual(len(self.service.get_default_players()), 6)
        self.assertEqual(self.service.get_default_players()[0], "samushka")

    def test_get_default_player_colors(self):
        self.assertEqual(len(self.service.get_default_player_colors()), 6)
        self.assertEqual(self.service.get_default_player_colors()[0], "IndianRed1")

    def test_get_default_board_sizes(self):
        self.assertEqual(len(self.service.get_default_board_sizes()), 6)
        self.assertEqual(self.service.get_default_board_sizes()[5][0], "The Ultimate Challenge")
        self.assertEqual(self.service.get_default_board_sizes()[5][1], 30)

    def test_get_categories(self):
        self.assertEqual(len(self.service.get_categories()), 3)
        self.assertEqual(self.service.get_categories()[1], "Random (Open Trivia DB)")

    def test_get_default_category_colors(self):
        self.assertEqual(len(self.service.get_default_category_colors()), 12)
        self.assertEqual(self.service.get_default_category_colors()[0], "black")

    def test_get_default_difficulties(self):
        self.assertEqual(len(self.service.get_default_difficulties()), 3)
        self.assertEqual(self.service.get_default_difficulties()[0], "Easy")

    def test_collect_player_settings(self):
        entry_field_1 = combobox()
        entry_field_2 = combobox()
        entry_field_3 = combobox()
        entry_field_4 = combobox()
        entry_field_1.set("samushka")
        entry_field_2.set("Add player")
        entry_field_3.set("")
        entry_field_4.set("Player 4")
        added_players = [
            entry_field_1,
            entry_field_2,
            entry_field_3,
            entry_field_4,
        ]
        self.assertEqual(len(self.service.collect_player_settings(added_players)), 2)
        self.assertEqual(self.service.collect_player_settings(added_players)[0], "samushka")
        self.assertEqual(self.service.collect_player_settings(added_players)[1], "Player 4")

    def test_collect_player_color_settings(self):
        self.assertEqual(len(self.service.collect_player_color_settings()), 6)
        self.assertEqual(self.service.collect_player_color_settings()[0], "IndianRed1")

    def test_collect_category_settings(self):
        entry_field_1 = combobox()
        entry_field_2 = combobox()
        entry_field_3 = combobox()
        entry_field_1.set("Movies")
        entry_field_2.set("Add category")
        entry_field_3.set("TV")
        added_categories = [
            entry_field_1,
            entry_field_2,
            entry_field_3,
        ]
        self.assertEqual(len(self.service.collect_category_settings(added_categories)), 2)
        self.assertEqual(self.service.collect_category_settings(added_categories)[0], "Movies")
        self.assertEqual(self.service.collect_category_settings(added_categories)[1], "TV")

    def test_collect_category_color_settings(self):
        self.assertEqual(len(self.service.collect_category_color_settings()), 12)
        self.assertEqual(self.service.collect_category_color_settings()[0], "black")

    def test_collect_board_size_settings(self):
        selected_board_size = combobox()
        selected_board_size.set("Medium")
        self.assertEqual(self.service.collect_board_size_settings(selected_board_size), 5)

    def test_check_settings_validity(self):
        self.assertEqual(self.service.check_settings_validity(), False)

    def test_check_player_number_validity(self):
        self.assertEqual(self.service.check_player_number_validity(), False)

    def test_check_player_names_validity(self):
        self.assertEqual(self.service.check_player_names_validity(), True)

    def test_check_category_number_validity(self):
        self.assertEqual(self.service.check_category_number_validity(), False)

    def test_check_otdb_connection_is_working(self):
        self.assertEqual(self.service.check_otdb_connection(), True)

    def test_check_otdb_connection_is_not_working(self):
        self.assertEqual(self.service.check_otdb_connection(0.0001), False)

    def test_handle_session_save(self):
        self.assertEqual(
            self.service.handle_session_save(
                [self.user], [self.question.category, self.question.category], 5),
            None,
        )

    def test_handle_logout(self):
        self.assertEqual(len(self.database.get_logged_in_user()), 1)
        self.service.logout_users()
        self.assertEqual(len(self.database.get_logged_in_user()), 0)
