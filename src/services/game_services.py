import random
from repositories.database_services import database_services as default_database


class GameServices:
    """Class constructor that initializes a new game service.

    Attributes:
        database: Value of the current database.
    """
    def __init__(self, database=default_database):
        """Class constructor that initializes a new game service.
        It fetches the necessary game session variables
        by calling a database class method.

        Args:
            database: Value of the current database.
        """
        self.database = database
        self.board_size = self.database.get_session_variables()[1]
        self.players = self.database.get_session_variables()[2]
        self.categories = self.database.get_session_variables()[3]
        self.current_turn = 0
        self.current_category = None
        self.current_question = None
        self.laps = [0, 0, 0, 0, 0, 0]
        self.player_points = []

    def get_difficulty(self):
        """Provides the selected difficulty for the game session.

        Returns:
            An integer value describing the difficulty.
        """
        difficulty = self.database.get_session_variables()[0]

        return difficulty

    def get_board_size(self):
        """Provides the selected board size for the game session.

        Returns:
            An integer value describing the board size.
        """
        self.board_size = self.database.get_session_variables()[1]

        return self.board_size

    def get_players(self):
        """Provides the selected players for the game session.

        Returns:
            A list of string values describing player names.
        """
        self.players = self.database.get_session_variables()[2]

        return self.players

    def get_categories(self):
        """Provides the selected categories for the game session.

        Returns:
            A list of string values describing category names.
        """
        self.categories = self.database.get_session_variables()[3]

        return self.categories

    def calculate_segment_size(self):
        """Calculates the size of an individual board segment.

        Returns:
            An integer value of the segment size.
        """
        return 360 / self.calculate_number_of_segments()

    def calculate_number_of_segments(self):
        """Calculates the number of board segments.
        The operation consists of the starting segment
        plus the number of the other categories times
        the selected board size.

        Returns:
            An integer value of the number of segments.
        """
        return 1 + len(self.categories[1:]) * self.board_size

    def list_all_category_segments(self):
        """Provides the places of categories on the board.
        The first value of the categories is excluded,
        as it represents the unique starting segment.

        Returns:
            A nested list of integers of the places of categories on the board.
        """
        all_category_segments = []
        i = 0
        while i < len(self.categories[1:]):
            j = 0
            k = 1 + i
            category_segments = []
            while j <= self.board_size:
                category_segments.append(k)
                k += len(self.categories[1:])
                j += 1
            i += 1
            all_category_segments.append(category_segments)

        return all_category_segments

    def count_laps(self, player, starting_position, new_position):
        """Counts the laps player tokens have travelled during the session.

        Args:
            player (int): The current player.
            starting_position (int): The player token's starting position.
            new_position (int): The player token's new position.

        Returns:
            (int): The player token's corrected position.
        """
        if new_position <= 0:
            while new_position <= 0:
                new_position += 360
                self.laps[player] += 1
            starting_position[player] = new_position

        return new_position

    def get_laps(self):
        """Provides the number of laps player tokens have travelled during the session.

        Returns:
            (list): The number of laps per player.
        """
        return self.laps

    def get_die_faces(self):
        """Provides the images and numbers of the die.

        Returns:
            A list of tuples describing the die face image paths and numbers.
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

    def get_category_for_player(self):
        """Provides a category for the player.

        Returns:
            (str): The current category.
        """
        # This should actually be determined by the player's position on the game board.
        # I.e. this will be replaced by another solution for the final deadline.
        # -------------------------------------------------------------------------------
        self.current_category = random.choice(range(len(self.categories)))
        return self.categories[self.current_category]
        # -------------------------------------------------------------------------------

    def get_current_category_index(self):
        """Provides the current category index.

        Returns:
            (int): The current category index.
        """
        return self.current_category

    def get_question_for_player(self):
        """Provides a question from the selected category by
        calling a database services class method.

        Returns:
            (str): The question as a string value.
        """
        self.current_question = self.database.get_question_for_player(
            self.categories[self.current_category].replace("'", "''"))

        return self.current_question['question']

    def get_answer_for_player(self):
        """Provides an answer to the selected question by
        calling a database services class method.

        Returns:
            (str): The current answer.
        """
        answer = self.database.get_answer_for_player(
            self.current_question['question'].replace("'", "''"))

        return answer['answer']

    def update_current_turn(self):
        """Updates the turn counter to point to the next player.
        The counter resets when it equals the number of players.

        Returns:
            (int): The index value of the player whose turn it is.
        """
        self.current_turn += 1
        if self.current_turn == len(self.players):
            self.current_turn = 0

        return self.get_current_turn()

    def get_current_turn(self):
        """Provides the number describing the current turn.

        Returns:
            (int): The index value of the player whose turn it is.
        """
        return self.current_turn

    def get_default_player_points(self):
        """Provides default player points.

        Returns:
            player_points (list): The default player points.
        """
        for player in range(len(self.players)):
            for category in range(len(self.categories)):
                self.player_points.append((player, category, 0))

        return self.player_points

    def add_point_to_player(self):
        """Provides updated player points.

        Returns:
            player_points (list): The updated player points.
        """
        no_point = (self.current_turn, self.current_category, 0)
        give_point = (self.current_turn, self.current_category, 1)

        for i in range(len(self.player_points)):
            if self.player_points[i] == no_point:
                self.player_points[i] = give_point

        return self.player_points

    def remove_point_from_player(self):
        """Provides updated player points.

        Returns:
            player_points (list): The updated player points.
        """
        has_point = (self.current_turn, self.current_category, 1)
        remove_point = (self.current_turn, self.current_category, 0)

        for i in range(len(self.player_points)):
            if self.player_points[i] == has_point:
                self.player_points[i] = remove_point

        return self.player_points

    def remove_game_active_status(self):
        """Calls a database service method which
        removes the current game's active status.
        """
        self.database.remove_game_active_status()
