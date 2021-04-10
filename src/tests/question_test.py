import unittest
from entities.question import Question

class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question = Question(
            "Computer Science",
            "Easy",
            "What is 'python'?",
            "A programming language",
        )

    def test_created_question_exists(self):
        self.assertNotEqual(self.question, None)

    def test_created_category_is_set_correctly(self):
        self.assertEqual(str(self.question.category), "Computer Science")

    def test_created_difficulty_is_set_correctly(self):
        self.assertEqual(str(self.question.difficulty), "Easy")

    def test_created_question_is_set_correctly(self):
        self.assertEqual(str(self.question.question), "What is 'python'?")

    def test_created_answer_is_set_correctly(self):
        self.assertEqual(str(self.question.answer), "A programming language")
