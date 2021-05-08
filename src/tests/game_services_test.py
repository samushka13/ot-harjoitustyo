import unittest
from config import TEST_DATABASE_FILENAME as test_database
from repositories.database_services import DatabaseServices
from services.game_services import GameServices
from entities.question import Question
from entities.game import Game
from entities.player import Player


class TestGameServices(unittest.TestCase):
    def setUp(self):
        # ---------------------------------------------------------------------
        # First the test database is cleared just to be sure it's empty.
        # ---------------------------------------------------------------------
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Questions")
        DatabaseServices(test_database).database.execute("DROP TABLE IF EXISTS Games")
        # ---------------------------------------------------------------------
        # Then the database and other entities are initialized to ease testing.
        # ---------------------------------------------------------------------
        self.database = DatabaseServices(test_database)
        self.question = Question(1, "TV", "Easy", "Question?", "Answer!")
        self.question_2 = Question(1, "Movies", "Easy", "What?", "Yeah!")
        self.question_3 = Question(1, "Sports", "Easy", "What?", "Yeah!")
        for question in [self.question, self.question_2, self.question_3]:
            self.database.save_question_item(
                question.user_id,
                question.category,
                question.difficulty,
                question.question,
                question.answer,
            )
        self.player = Player("samushka", "red", [(0,0,0), (0,1,0)], [0], [360])
        self.game = Game(1, "Easy", 1, [self.player.name, "player 2"], ["TV", "Movies", "Sports"])
        self.database.save_session_variables(
          self.game.difficulty,
          self.game.board_size,
          self.game.players,
          self.game.categories,
        )
        self.service = GameServices(self.database)

    def test_settings_are_correct(self):
        self.assertEqual(self.service.difficulty, "Easy")
        self.assertEqual(len(self.service.players), 2)
        self.assertEqual(self.service.players[0], "samushka")
        self.assertEqual(self.service.board_size, 1)
        self.assertEqual(len(self.service.categories), 3)
        self.assertEqual(self.service.categories[0], "TV")

    def test_calculate_segment_size(self):
        self.assertEqual(self.service.calculate_segment_size(), 120)

    def test_calculate_number_of_segments(self):
        self.assertEqual(self.service.calculate_number_of_segments(), 3)

    def test_get_category_places(self):
        self.assertEqual(self.service.get_category_places(), [[1], [2]])

    def test_update_player_positions_radii(self):
        self.assertEqual(
            self.service.update_player_positions_radii(0,0), [360, 360, 360, 360, 360, 360]
        )
        self.assertEqual(
            self.service.update_player_positions_radii(1,3), [360, 360, 360, 360, 360, 360]
        )
        self.assertEqual(
            self.service.update_player_positions_radii(0,6), [360, 360, 360, 360, 360, 360]
        )
        self.assertEqual(
            self.service.update_player_positions_radii(1,1), [360, 240, 360, 360, 360, 360]
        )

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

    def test_get_question_for_player_flow_with_different_categories(self):
        questions = [self.question, self.question_2, self.question_3]
        for i in range(len(self.game.categories)):
            self.service.player_positions_indices = [i,0,0,0,0,0]
            self.service.current_category_index = i
            category = self.service.get_category_for_player()
            question = self.service.get_question_for_player()
            answer = self.service.get_answer_for_player()
            self.assertEqual(category == self.game.categories[i], True)
            self.assertEqual(question == questions[i].question, True)
            self.assertEqual(answer == questions[i].answer, True)
            self.assertEqual(self.service.current_category_index, i)

    def test_update_current_turn(self):
        self.assertEqual(self.service.current_turn, 0)
        self.assertEqual(self.service.update_current_turn(), 1)
        self.assertEqual(self.service.current_turn, 1)
        self.assertEqual(self.service.update_current_turn(), 0)
        self.assertEqual(self.service.current_turn, 0)

    def test_get_default_player_points(self):
        points = [(0,0,0), (0,1,0), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.assertEqual(self.service.get_default_player_points(), points)

    def test_add_point_to_player(self):
        self.service.get_default_player_points()
        self.service.current_category_index = 0
        updated_points = [(0,0,1), (0,1,0), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.assertEqual(self.service.add_point_to_player(), updated_points)

    def test_remove_point_from_player(self):
        self.service.player_points = [(0,0,1), (0,1,0), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.service.current_category_index = 0
        updated_points = [(0,0,0), (0,1,0), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.assertEqual(self.service.remove_point_from_player(), updated_points)

    def test_check_victory_condition_with_not_enough_points_and_not_crossing_the_finish_line(self):
        self.service.player_points = [(0,0,1), (0,1,1), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.service.current_turn = 0
        self.service.laps[self.service.current_turn] = 0
        self.assertEqual(self.service.check_victory_condition(0), False)

    def test_check_victory_condition_with_not_enough_points_but_crossing_the_finish_line(self):
        self.service.player_points = [(0,0,1), (0,1,1), (0,2,0), (1,0,0), (1,1,0), (1,2,0)]
        self.service.current_turn = 1
        self.service.laps[self.service.current_turn] = 1
        self.assertEqual(self.service.check_victory_condition(0), False)

    def test_check_victory_condition_with_enough_points_but_not_crossing_the_finish_line(self):
        self.service.player_points = [(0,0,1), (0,1,1), (0,2,1), (1,0,0), (1,1,0), (1,2,0)]
        self.service.current_turn = 0
        self.service.laps[self.service.current_turn] = 0
        self.assertEqual(self.service.check_victory_condition(0), False)

    def test_check_victory_condition_with_enough_points_and_crossing_the_finish_line(self):
        self.service.player_points = [(0,0,1), (0,1,1), (0,2,1), (1,0,0), (1,1,0), (1,2,0)]
        self.service.current_turn = 0
        self.service.laps[self.service.current_turn] = 1
        self.assertEqual(self.service.check_victory_condition(0), True)

    def test_remove_game_active_status(self):
        self.assertEqual(self.service.remove_game_active_status(), None)
