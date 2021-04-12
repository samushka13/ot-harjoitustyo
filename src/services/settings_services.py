class SettingsServices():
    """Class that describes all services related to game settings.

    Attributes:
        current_user: String value of the user's username.
    """

    def __init__(self, current_user, database):
        """Class constructor that creates a new settings service.

        Args:
            current_user: String value of the user's username.
        """

        self.current_user = current_user
        self.database = database

    def get_default_players(self):
        """Returns default player names.

        The UI only accommodates six players,
        so increasing the number here would require changes in the UI as well.
        """

        default_players = [
            f"{self.current_user}",
            "Player 2",
            "Player 3",
            "Player 4",
            "Player 5",
            "Player 6",
        ]
        return default_players

    def get_default_player_colors(self):
        """Returns default player colors.

        The UI only accommodates six players,
        so increasing the number here would require changes in the UI as well.
        """

        default_player_colors = [
            "red",
            "brown",
            "green",
            "purple",
            "orange",
            "blue",
        ]
        return default_player_colors

    def get_default_board_sizes(self):
        """Returns default board sizes.

        The app logic has been made to accommodate changes here,
        so adding more options, for example, is possible.

        However, it is not practical to give a size larger than 30,
        as the board segments will become too small to see properly,
        if all twelve categories are selected in game settings.
        """

        board_sizes = [
            ("Tiny (least difficult)", 1),
            ("Small", 3),
            ("Medium", 5),
            ("Large", 7),
            ("Insane", 9),
            ("The Ultimate Challenge", 30)
        ]
        return board_sizes

    def get_categories(self):
        return self.database.get_categories()

    def get_item_for_editing(self):
        return self.database.get_item_for_editing()

    def update_item(self):
        return self.database.update_item()

    def get_default_category_colors(self):
        """Returns default category colors.

        The UI only accommodates 12 categories,
        so increasing the number here would require changes in the UI as well.
        """

        category_colors = [
            "black",
            "red",
            "gold",
            "green",
            "purple",
            "orange",
            "blue",
            "grey",
            "brown",
            "pink",
            "magenta",
            "turquoise",
        ]
        return category_colors

    def get_default_difficulties(self):
        """Returns default difficulty names.

        The app logic can handle adding more options,
        but the game has been designed to have only three difficulty levels.
        """

        difficulty_names = [
            "Easy",
            "Intermediate",
            "Advanced Triviliast"
        ]
        return difficulty_names
