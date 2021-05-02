import unittest
import tkinter as tk
from repositories.database_services import DatabaseServices
from services.custom_content_services import CustomContentServices
from entities.user import User
from entities.question import Question
from config import TEST_DATABASE_FILENAME as test_database
from ui.widgets import get_listbox


class TestCustomContentServices(unittest.TestCase):
    def setUp(self):
        # ---------------------------------------------------------------------
        # First the test database is cleared just to be sure it's empty.
        # ---------------------------------------------------------------------
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Users")
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Questions")
        # ---------------------------------------------------------------------
        # Then the services and test database are initialized.
        # ---------------------------------------------------------------------
        self.database = DatabaseServices(test_database)
        self.service = CustomContentServices(self.database)
        # ---------------------------------------------------------------------
        # Finally some stuff is added to the database to ease test formulation.
        # ---------------------------------------------------------------------
        self.user = User("samushka", "13")
        self.database.add_user(self.user.username, self.user.password)
        self.database.add_logged_in_user(self.user.username)
        self.question = Question(1, "Category", "Difficulty", "Question?", "Answer!")
        self.question_invalid = Question(2, "", "", "", "")
        self.database.save_item_to_database(
            self.question.user_id,
            self.question.category,
            self.question.difficulty,
            self.question.question,
            self.question.answer,
        )

    def test_database_exists(self):
        self.assertNotEqual(self.database, None)

    def test_get_listbox_items(self):
        self.assertEqual(
            self.service.get_listbox_items(),
            ["1. | Category | Difficulty | Question? | Answer! ||| samushka"],
        )

    def test_get_categories(self):
        self.assertEqual(self.service.get_categories(), ["Category"])

    def test_get_difficulties(self):
        self.assertEqual(
            self.service.get_difficulties(),
            ["Easy", "Intermediate", "Advanced Triviliast"],
        )

    def test_get_current_user_id(self):
        self.assertEqual(self.service.get_current_user_id(), 1)

    def test_check_input_validity(self):
        self.assertEqual(
            self.service.check_input_validity(
                self.question.category,
                self.question.difficulty,
                self.question.question,
                self.question.answer,
            ),
            True,
        )
        self.assertEqual(
            self.service.check_input_validity(
                self.question_invalid.category,
                self.question_invalid.difficulty,
                self.question_invalid.question,
                self.question_invalid.answer,
            ),
            False,
        )

    def test_format_question(self):
        self.assertEqual(self.service.format_question(self.question.question), "Question?")
        self.assertEqual(self.service.format_question("Question"), "Question?")

    def test_format_answer(self):
        self.assertEqual(self.service.format_answer(self.question.answer), "Answer!")
        self.assertEqual(self.service.format_answer("Answer."), "Answer.")
        self.assertEqual(self.service.format_answer("Answer"), "Answer.")

    def test_handle_save_item(self):
        self.assertEqual(
            self.service.handle_save_item(
                self.question.category,
                self.question.difficulty,
                self.question.question,
                self.question.answer,
            ),
            None,
        )
        self.assertEqual(self.database.get_question(1, 1), 1)

    def test_check_owner(self):
        self.assertEqual(self.service.check_owner(1), True)
        self.assertEqual(self.service.check_owner(2), False)

    def test_determine_question_ids(self):
        listbox = get_listbox()
        for entry in self.service.get_listbox_items():
            listbox.insert(tk.END, entry)
            listbox.select_set(0)
        self.assertEqual(self.service.determine_question_ids(listbox), ["1."])

    def test_count_questions(self):
        self.assertEqual(self.service.count_questions(), 1)

    def test_delete_items(self):
        self.assertEqual(self.service.delete_items(["1."]), 1)

    def test_delete_all(self):
        question = Question(1, "Category", "Difficulty", "Question?", "Answer!")
        self.database.save_item_to_database(
            question.user_id,
            question.category,
            question.difficulty,
            question.question,
            question.answer,
        )
        self.assertEqual(self.service.delete_all(), None)
        self.assertEqual(self.database.get_question(1, 1), 0)

    def test_get_item_for_editing(self):
        self.question = Question(1, "Category", "Difficulty", "Question?", "Answer!")
        self.database.save_item_to_database(
            self.question.user_id,
            self.question.category,
            self.question.difficulty,
            self.question.question,
            self.question.answer,
        )
        self.assertEqual(
            self.service.get_item_for_editing(1),
            ("Category", "Difficulty", "Question?", "Answer!"),
        )

    def test_update_item(self):
        self.assertEqual(
            self.service.update_item(
                1,
                "Category",
                "Difficulty",
                "Question?",
                "The updated answer.",
            ),
            None,
        )
        self.assertEqual(self.database.get_item_for_editing(1)[3], "The updated answer.")
