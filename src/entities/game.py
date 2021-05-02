class Game:
    """Class that describes an individual game session.

    Attributes:
        user_id: An integer value of the user's id.
        difficulty: String value of the game's difficulty.
        board_size: Integer value of the game's board size.
        players: List of players.
        categories: List of categories.
    """

    def __init__(self, user_id, difficulty, board_size, players, categories):
        """Class constructor that initiates a new game session.

        Args:
            user_id: An integer value of the user's id.
            difficulty: String value of the game's difficulty.
            board_size: Integer value of the game's board size.
            players: List of players.
            categories: List of categories.
        """

        self.user_id = user_id
        self.difficulty = difficulty
        self.board_size = board_size
        self.players = players
        self.categories = categories
