class Game:
    """Class that describes an individual game session.

    Attributes:
        user_id (int): The user's id.
        difficulty (str): The selected difficulty.
        board_size (int): The selected board size.
        players (list): The selected players.
        categories (list): The selected categories.
    """

    def __init__(self, user_id, difficulty, board_size, players, categories):
        """Class constructor that initializes a new game session.

        Args:
            user_id (int): The user's id.
            difficulty (str): The selected difficulty.
            board_size (int): The selected board size.
            players (list): The selected players.
            categories (list): The selected categories.
        """

        self.user_id = user_id
        self.difficulty = difficulty
        self.board_size = board_size
        self.players = players
        self.categories = categories
