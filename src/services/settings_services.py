from repositories.database_services import database_services as default_database


class SettingsServices:
    """Class that describes all services related to game settings.

    Attributes:
        database: Value of the current database.
    """

    def __init__(self, database=default_database):
        """Class constructor that creates a new settings service.

        Args:
            database: Value of the current database.
        """

        self.database = database
        self.players = []
        self.player_colors = []
        self.categories = []
        self.category_colors = []
        self.difficulty_names = []
        self.board_size = None

    # ---------------------------------------------------------
    # Methods that provide default settings for game sessions:
    # ---------------------------------------------------------

    def get_default_players(self):
        """Provides a list of default player names.

        The UI only accommodates six players,
        so increasing the number here would require changes in the UI as well.

        Returns:
            A list of the default player names.
            The first name is the current user's username.
        """

        default_players = [
            f"{self.database.get_logged_in_user()[0][1]}",
            "Player 2",
            "Player 3",
            "Player 4",
            "Player 5",
            "Player 6",
        ]
        return default_players

    def get_default_player_colors(self):
        """Provides a list of default player colors.

        The UI only accommodates six players,
        so increasing the number here would require changes in the UI as well.

        Returns:
            A list of the default player colors.
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
        """Provides a list of default board sizes.

        The integer after the string determines how many times
        each category is represented on the game board.
        Game difficulty rises as the integer value increases.

        The app logic has been made to accommodate changes here
        (or even implementing a way to let the user select the size freely),
        so adding more options, for example, is possible.

        However, it is not practical to give a size larger than 30,
        as the board segments will become too small to perceive properly,
        if all twelve categories are selected in game settings.

        Returns:
            A list of the default board sizes.
        """

        board_sizes = [
            ("Tiny", 1),
            ("Small", 3),
            ("Medium", 5),
            ("Large", 7),
            ("Insane", 9),
            ("The Ultimate Challenge", 30)
        ]
        return board_sizes

    def get_categories(self):
        """Calls a database class method that fetches all existing categories.

        Returns:
            The result of the method call, which consists of
            a list of string values of the categories.
        """

        return self.database.get_categories()

    def get_default_category_colors(self):
        """Provides a list of default category colors.

        The UI only accommodates 12 categories,
        so increasing the number here would require changes in the UI as well.

        Returns:
            A list of the default category colors.
        """

        self.category_colors = [
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
        return self.category_colors

    def get_default_difficulties(self):
        """Provides a list of default difficulty names.

        The app logic can handle adding more options,
        but the game has been designed to have only three difficulty levels.
        Therefore, changing this is not recommended.

        Returns:
            A list of the default difficulty names.
        """

        self.difficulty_names = [
            "Easy",
            "Intermediate",
            "Advanced Triviliast"
        ]

        return self.difficulty_names

    # --------------------------------------------------
    # Methods that collect settings for a game session:
    # --------------------------------------------------

    def collect_player_settings(self, added_players):
        """Provides a list of player names from user inputs.

        Args:
            added_players: A list of string values describing the selected players.

        Returns:
            A list of string values of player names.
        """

        self.players = []
        for entry in added_players:
            if entry.get() != "" and entry.get() != "Add player":
                self.players.append(entry.get())

        return self.players

    def collect_player_color_settings(self):
        """Provides a list of player colors from default values.
        Can be expanded so that it takes the values from user inputs,
        when the UI accommodates such a feature.

        Returns:
            A list of values of player colors.
        """

        return self.get_default_player_colors()

    def collect_category_settings(self, added_categories):
        """Provides a list of category names from user inputs.

        Args:
            added_categories: A list of string values describing the selected categories.

        Returns:
            A list of string values of category names.
        """

        self.categories = []
        for category in added_categories:
            if category.get() != "" and category.get() != "Add category":
                self.categories.append(category.get())

        return self.categories

    def collect_category_color_settings(self):
        """Provides a list of category colors from default values.
        Can be expanded so that it takes the values from user inputs,
        when the UI accommodates such a feature.

        Returns:
            A list of values of category colors.
        """

        return self.get_default_category_colors()

    def collect_board_size_settings(self, selected_board_size):
        """Provides the board size from user input.

        Args:
            selected_board_size: A string value describing the board size.

        Returns:
            An integer value describing the board size.
        """

        for i in range(0, len(self.get_default_board_sizes())):
            if selected_board_size.get() == [x[0] for x in self.get_default_board_sizes()][i]:
                self.board_size = [x[1] for x in self.get_default_board_sizes()][i]

        return self.board_size

    def handle_session_save(self, players, categories, board_size):
        """Calls database class methods which ensure that no other game session is active
        and then save the current game session variables to the database.

        Args:
            players (list): The selected players.
            categories (list): The selected categories.
            board_size (int): The selected board size.
        """

        self.database.remove_game_active_status()
        difficulty = ""
        self.database.save_session_variables(
            difficulty,
            board_size,
            players,
            categories,
        )

    # ------------------------------------------------------
    # Methods that check the validity of the game settings:
    # ------------------------------------------------------

    def check_player_number_validity(self):
        """Checks if enough players were added.

        Returns:
            True, if it was, or False, if not.
        """

        return bool(len(self.players) > 0)

    def check_player_names_validity(self):
        """Checks if the added player names are unique.

        Returns:
            True, if they are, or False, if they aren't.
        """

        return bool(len(set(self.players)) == len(self.players))

    def check_category_number_validity(self):
        """Checks if enough categories were added.

        Returns:
            True, if it was, or False, if not.
        """

        return bool(len(self.categories) >= 2)

    def logout_users(self):
        """Calls a DatabaseServices class method to remove all logged in users
        (currently only one simultaneous login is allowed, but this method can handle more)."""

        return self.database.remove_logged_in_users()


settings_services = SettingsServices()
