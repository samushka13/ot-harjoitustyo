import unittest
from config import TEST_DATABASE_FILENAME as test_database
from repositories.database_services import DatabaseServices
from services.game_services import GameServices
from entities.question import Question
from entities.game import Game


class TestGameServices(unittest.TestCase):
    def setUp(self):
        # ---------------------------------------------------------------------
        # First the test database is cleared just to be sure it's empty.
        # ---------------------------------------------------------------------
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Questions")
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Games")
        # ---------------------------------------------------------------------
        # Then the services and test database are initialized and
        # some stuff is added to the database to ease test formulation.
        # ---------------------------------------------------------------------
        self.database = DatabaseServices(test_database)
        self.question = Question(1, "TV Shows", "Easy", "Question?", "Answer!")
        self.database.save_question_item(
            self.question.user_id,
            self.question.category,
            self.question.difficulty,
            self.question.question,
            self.question.answer,
        )
        self.question_2 = Question(2, "Movies", "Easy", "What?", "Yeah!")
        self.database.save_question_item(
            self.question_2.user_id,
            self.question_2.category,
            self.question_2.difficulty,
            self.question_2.question,
            self.question_2.answer,
        )
        self.game = Game(1, "Easy", 3, ["samushka", "bbb", "ccc"], ["TV Shows", "Movies"])
        self.database.save_session_variables(
          self.game.difficulty,
          self.game.board_size,
          self.game.players,
          self.game.categories,
        )
        self.service = GameServices(self.database)

    def test_difficulty_set_correctly(self):
        self.assertEqual(self.service.difficulty, "Easy")

    def test_players_set_correctly(self):
        self.assertEqual(len(self.service.players), 3)
        self.assertEqual(self.service.players[0], "samushka")

    def test_board_size_set_correctly(self):
        self.assertEqual(self.service.board_size, 3)

    def test_categories_set_correctly(self):
        self.assertEqual(len(self.service.categories), 2)
        self.assertEqual(self.service.categories[0], "TV Shows")

    def test_calculate_segment_size(self):
        self.assertEqual(self.service.calculate_segment_size(), 90)

    def test_calculate_number_of_segments(self):
        self.assertEqual(self.service.calculate_number_of_segments(), 4)

    def test_list_all_category_segments(self):
        self.assertEqual(self.service.list_all_category_segments(), [[1, 2, 3, 4]])

    def test_update_player_positions(self):
        self.assertEqual(self.service.update_player_positions(0,0), [360, 360, 360, 360, 360, 360])
        self.assertEqual(self.service.update_player_positions(1,3), [360, 90, 360, 360, 360, 360])
        self.assertEqual(self.service.update_player_positions(0,6), [180, 90, 360, 360, 360, 360])
        self.assertEqual(self.service.update_player_positions(1,3), [180, 180, 360, 360, 360, 360])
        self.assertEqual(self.service.update_player_positions(0,6), [360, 180, 360, 360, 360, 360])
        self.assertEqual(self.service.update_player_positions(1,3), [360, 270, 360, 360, 360, 360])

    def test_count_and_get_laps(self):
        self.assertEqual(self.service.laps, [0, 0, 0, 0, 0, 0])
        self.assertEqual(self.service.count_laps(0, [360, 360, 360, 360, 360, 360], 0), 360)
        self.assertEqual(self.service.laps, [1, 0, 0, 0, 0, 0])
        self.assertEqual(self.service.count_laps(1, [360, 360, 360, 360, 360, 360], -720), 360)
        self.assertEqual(self.service.laps, [1, 3, 0, 0, 0, 0])
        self.assertEqual(self.service.count_laps(1, [360, 360, 360, 360, 360, 360], 180), 180)
        self.assertEqual(self.service.laps, [1, 3, 0, 0, 0, 0])

    def test_get_die_faces(self):
        self.assertEqual(self.service.get_die_faces()[0][1], 1)

    def test_get_die_face(self):
        self.assertEqual(self.service.get_die_face()[1] in range(1,7), True)

    def test_get_question_for_player_flow(self):
        category = self.service.get_category_for_player()
        question = self.service.get_question_for_player()
        answer = self.service.get_answer_for_player()

        self.assertEqual(category in self.game.categories, True)
        self.assertEqual(self.service.current_category in range(len(self.game.categories)), True)
        self.assertEqual(question in (self.question.question, self.question_2.question), True)
        self.assertEqual(answer in (self.question.answer, self.question_2.answer), True)

    def test_update_current_turn(self):
        self.assertEqual(self.service.current_turn, 0)
        self.assertEqual(self.service.update_current_turn(), 1)
        self.assertEqual(self.service.current_turn, 1)
        self.assertEqual(self.service.update_current_turn(), 2)
        self.assertEqual(self.service.current_turn, 2)
        self.assertEqual(self.service.update_current_turn(), 0)
        self.assertEqual(self.service.current_turn, 0)

    def test_get_default_player_points(self):
        points = [(0,0,0), (0,1,0), (1,0,0), (1,1,0), (2,0,0), (2,1,0)]
        self.assertEqual(self.service.get_default_player_points(), points)

    def test_add_point_to_player(self):
        self.service.get_default_player_points()
        self.service.current_category = 0
        updated_points = [(0,0,1), (0,1,0), (1,0,0), (1,1,0), (2,0,0), (2,1,0)]
        self.assertEqual(self.service.add_point_to_player(), updated_points)

    def test_remove_point_from_player(self):
        self.service.player_points = [(0,0,1), (0,1,0), (1,0,0), (1,1,0), (2,0,0), (2,1,0)]
        self.service.current_category = 0
        updated_points = [(0,0,0), (0,1,0), (1,0,0), (1,1,0), (2,0,0), (2,1,0)]
        self.assertEqual(self.service.remove_point_from_player(), updated_points)

    def test_remove_game_active_status(self):
        self.assertEqual(self.service.remove_game_active_status(), None)
