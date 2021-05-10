import random
import html
import requests
from repositories.database_services import database_services as default_database


class GameServices:
    """Class that describes all game-related services.

    Attributes:
        database: The current database.
    """

    def __init__(self, database=default_database):
        """Class constructor that initializes a new game service by
        setting up the necessary attributes for a game session.

        Args:
            database: The current database.
        """

        self.database = database
        self.difficulty = self.database.get_session_variables()[0]
        self.board_size = self.database.get_session_variables()[1]
        self.players = self.database.get_session_variables()[2]
        self.categories = self.database.get_session_variables()[3]
        self.current_turn = 0
        self.current_category_index = None
        self.current_question = None
        self.otdb_question_item = None
        self.laps = [0, 0, 0, 0, 0, 0]
        self.player_positions_radii = [360, 360, 360, 360, 360, 360]
        self.player_positions_indices = [0, 0, 0, 0, 0, 0]
        self.player_points = []

    def calculate_segment_size(self):
        """Calculates the size of an individual board segment.

        Returns:
            segment_size (int): The segment size.
        """

        segment_size = 360 / self.calculate_number_of_segments()

        return segment_size

    def calculate_number_of_segments(self):
        """Calculates the number of board segments.
        The operation consists of the starting segment plus
        the number of other categories times the selected board size.

        Returns:
            segments (int): The number of segments.
        """

        segments = 1 + len(self.categories[1:]) * self.board_size

        return segments

    def get_category_places(self):
        """Provides the places of categories on the board.
        The first value of the categories is excluded,
        as it represents the unique starting segment.

        Returns:
            category_places (list): Lists of category segments as integers.
            Each nested list describes the positions of one of the categories on the game board.
        """

        category_places = []
        i = 0
        while i < len(self.categories[1:]):
            j = 0
            k = 1 + i
            category_segments = []
            while j < self.board_size:
                category_segments.append(k)
                k += len(self.categories[1:])
                j += 1
            i += 1
            category_places.append(category_segments)

        return category_places

    def update_player_positions_radii(self, player, number):
        """Keeps track of the players' positions on the game board,
        so that the UI knows where to draw the player tokens.
        Also calls another method which updates players' position indices.

        Args:
            player (int): The current player.
            number (int): The current die face.

        Returns:
            self.player_positions_radii (list): The players' current positions as radii.
        """

        new_position = self.player_positions_radii[player] - self.calculate_segment_size() * number
        self.player_positions_radii[player] = new_position
        self.count_laps(player, self.player_positions_radii, new_position)

        self._update_player_positions_indices(player, number)

        return self.player_positions_radii

    def _update_player_positions_indices(self, player, number):
        """Keeps track of the players' position indices on the game board,
        so that the game services can match the current player position with a category.

        Args:
            player (int): The current player.
            number (int): The current die face.

        Returns:
            self.player_positions_indices (list): The players' current positions as indices.
        """

        segments = self.calculate_number_of_segments()
        new_position_index = self.player_positions_indices[player] + number
        if new_position_index >= segments:
            while new_position_index >= segments:
                new_position_index -= segments
        self.player_positions_indices[player] = new_position_index

        return self.player_positions_indices

    def count_laps(self, player, starting_position, new_position):
        """Counts the laps player tokens have travelled during the session.

        Args:
            player (int): The current player.
            starting_position (int): The player token's starting position.
            new_position (int): The player token's new position.

        Returns:
            new_position (int): The player token's corrected position.
        """

        if new_position <= 0:
            while new_position <= 0:
                new_position += 360
                self.laps[player] += 1
            starting_position[player] = new_position

        return new_position

    def get_die_faces(self):
        """Provides the images and numbers of the die.

        Returns:
            die_faces (list): The die faces as tuples of image paths and numbers.
        """

        die_faces = [
            (r'src/assets/die_1.png', 1),
            (r'src/assets/die_2.png', 2),
            (r'src/assets/die_3.png', 3),
            (r'src/assets/die_4.png', 4),
            (r'src/assets/die_5.png', 5),
            (r'src/assets/die_6.png', 6),
        ]

        return die_faces

    def get_die_face(self):
        """Provides a random face of a six-sided die.

        Returns:
            die_face (tuple): A random die face as (image path, number).
        """

        die_face = random.choice(self.get_die_faces())

        return die_face

    def get_category_for_player(self):
        """Provides a category for the player based on
        the player token's current position.

        Calls the Open Trivia Database API for a question item,
        if the current category is not a custom category.

        Returns:
            category (str): The current category.
        """

        category_places = self.get_category_places()
        if self.player_positions_indices[self.current_turn] == 0:
            self.current_category_index = 0
        else:
            for nested_list in category_places:
                if self.player_positions_indices[self.current_turn] in nested_list:
                    self.current_category_index = category_places.index(nested_list)+1

        category = self.categories[self.current_category_index]

        if "Open Trivia" in category:
            self._get_otdb_question_item_category()

        return category

    def _get_otdb_question_item_category(self):
        """Calls the Open Trivia API to get a random question item and
        provides its category. 

        Returns:
            category (str): The current category.
        """

        self.otdb_question_item = requests.get("https://opentdb.com/api.php?amount=1")
        question_type = html.unescape(self.otdb_question_item.json()['results'][0]['type'])
        self.check_otdb_question_item_type(question_type)

        category = html.unescape(self.otdb_question_item.json()['results'][0]['category'])

        return category

    def check_otdb_question_item_type(self, question_type):
        """If the question type is 'true or false',
        a new call is made to get a bit more challenging question.

        Args:
            question_type (str): The type of the requested question.
        """

        if question_type == 'boolean':
            self.otdb_question_item = requests.get(
                "https://opentdb.com/api.php?amount=1&type=multiple"
            )

    def get_question_for_player(self):
        """Provides a question from the current category by calling
        a database services class method or using the question item
        from the Open Trivia Database API, depending on the category.

        Returns:
            self.current_question (str): The current question.
        """

        category = self.categories[self.current_category_index].replace("'", "''")

        if "Open Trivia" in category:
            self.current_question = self._get_otdb_question_item_question()
        else:
            self.current_question = self.database.get_question_for_player(category)

        return self.current_question

    def _get_otdb_question_item_question(self):
        """Provides the question of an Open Trivia Database question item.
        Also, formats the question so that the question's actual category is shown.

        Returns:
            formatted_question (str): The current question and its category.
        """

        category = html.unescape(self.otdb_question_item.json()['results'][0]['category'])
        question = html.unescape(self.otdb_question_item.json()['results'][0]['question'])
        formatted_question = f"{category}\n\n{question}"

        return formatted_question

    def get_answer_for_player(self):
        """Provides an answer to the current question by calling
        a database services class method or using the question item
        from the Open Trivia Database API, depending on the category.

        Returns:
            answer (str): The current answer.
        """

        category = self.categories[self.current_category_index].replace("'", "''")

        if "Open Trivia" in category:
            answer = html.unescape(self.otdb_question_item.json()['results'][0]['correct_answer'])
        else:
            answer = self.database.get_answer_for_player(self.current_question.replace("'", "''"))

        return answer

    def update_current_turn(self):
        """Updates the turn counter to point to the next player.
        The counter resets when it equals the number of players.

        Returns:
            self.current_turn (int): The index value of the player whose turn it is.
        """

        self.current_turn += 1
        if self.current_turn == len(self.players):
            self.current_turn = 0

        return self.current_turn

    def get_default_player_points(self):
        """Provides default player points.

        Returns:
            self.player_points (list): The default player points.
        """

        for player in range(len(self.players)):
            for category in range(len(self.categories)):
                self.player_points.append((player, category, 0))

        return self.player_points

    def add_point_to_player(self):
        """Provides updated player points by checking whether
        the player already has a point in the current category and
        then adding the point, if needed.

        Returns:
            self.player_points (list): The updated player points.
        """

        no_point = (self.current_turn, self.current_category_index, 0)
        give_point = (self.current_turn, self.current_category_index, 1)

        for i in range(len(self.player_points)):
            if self.player_points[i] == no_point:
                self.player_points[i] = give_point

        return self.player_points

    def remove_point_from_player(self):
        """Provides updated player points by checking whether
        the player already has a point in the current category and
        then removing the point, if needed.

        Returns:
            self.player_points (list): The updated player points.
        """

        has_point = (self.current_turn, self.current_category_index, 1)
        remove_point = (self.current_turn, self.current_category_index, 0)

        for i in range(len(self.player_points)):
            if self.player_points[i] == has_point:
                self.player_points[i] = remove_point

        return self.player_points

    def check_victory_condition(self, player_starting_laps):
        """Checks whether the current player's new position is on or over
        the unique starting segment, and, if it is, checks whether the
        player has all the required category points for winning the game.

        Returns:
            True, if the player is victorious, or False, if not.
        """

        if self.laps[self.current_turn] > player_starting_laps:
            current_player_points = []
            for i, player_points in enumerate(self.player_points):
                if player_points[0] == self.current_turn:
                    current_player_points.append(player_points)
            for i, current_player_point in enumerate(current_player_points):
                if current_player_point != (self.current_turn, i, 1):
                    return False
            return True

        return False

    def remove_game_active_status(self):
        """Calls a DatabaseService class method which
        removes the current game's active status."""

        self.database.remove_game_active_status()
