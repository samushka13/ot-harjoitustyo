import requests
from repositories.database_services import database_services as default_database


class SettingsServices:
    """Class that describes all settings-related services.

    Attributes:
        database (class): The current database.
    """

    def __init__(self, database=default_database):
        """Class constructor that creates a new settings service.

        Args:
            database (class): The current database.
        """

        self.database = database
        self.players = []
        self.player_colors = []
        self.categories = []
        self.category_colors = []
        self.difficulty_names = []
        self.board_size = None

    def get_default_players(self):
        """Provides a list of default player names.
        The first item is the current user's username.

        The UI currently only accommodates six players,
        so increasing the number here would require changes in the UI as well.

        Returns:
            default_players (list): The default player names as string values.
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
            default_player_colors (list): The player colors as string values.
        """

        default_player_colors = [
            "IndianRed1",
            "lime green",
            "DeepSkyBlue2",
            "gold",
            "DarkOrchid1",
            "chocolate1",
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
            board_sizes (list): The default board sizes as tuples.
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
        The list is appended with a string pointing to the Open Trivia DB questions
        as well as an empty string that helps the user clear a selection.

        Returns:
            categories (list): The category names as string values.
        """

        categories = sorted(self.database.get_categories())
        categories.append("Random (Open Trivia DB)")
        categories.append("")

        return categories

    def get_default_category_colors(self):
        """Provides a list of default category colors.

        The UI only accommodates 12 categories,
        so increasing the number here would require changes in the UI as well
        for the added colors to be actually shown.

        Returns:
            self.category_colors (list): The category colors as string values.
        """

        self.category_colors = [
            "black",
            "red2",
            "gold2",
            "green",
            "purple",
            "orange",
            "brown",
            "RoyalBlue3",
            "slate grey",
            "OrangeRed3",
            "maroon2",
            "cyan4",
        ]

        return self.category_colors

    def get_default_difficulties(self):
        """Provides a list of default difficulty names.

        The app logic can handle adding more options,
        but the game has been designed to have only three difficulty levels.
        Therefore, changing this is not recommended.

        Returns:
            self.difficulty_names (list): The difficulty names as string values.
        """

        self.difficulty_names = [
            "Easy",
            "Intermediate",
            "Advanced Triviliast"
        ]

        return self.difficulty_names

    def collect_player_settings(self, added_players):
        """Provides a list of player names from user inputs.
        Removes all empty and generic default values.

        Args:
            added_players (list): The selected player names as string values.

        Returns:
            self.players (list): The selected player names as string values.
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
            player_colors (list): The player colors as string values.
        """

        player_colors = self.get_default_player_colors()

        return player_colors

    def collect_category_settings(self, added_categories):
        """Provides a list of category names from user inputs.
        Removes all empty and generic default values.

        Args:
            added_categories (list): The selected categories as string values.

        Returns:
            self.categories (list): The string values of the selected category names.
        """

        self.categories = []
        for category in added_categories:
            if category.get() not in ("", "Add category"):
                self.categories.append(category.get())

        return self.categories

    def collect_category_color_settings(self):
        """Provides a list of category colors from default values.
        Can be expanded so that it takes the values from user inputs,
        when the UI accommodates such a feature.

        Returns:
            category_colors (list): The category colors as string values.
        """

        category_colors = self.get_default_category_colors()

        return category_colors

    def collect_board_size_settings(self, selected_board_size):
        """Provides the board size from user input.

        Args:
            selected_board_size (str): The name of the selected board size.

        Returns:
            self.board_size (int): The selected board size.
        """

        for i in range(0, len(self.get_default_board_sizes())):
            if selected_board_size.get() == [x[0] for x in self.get_default_board_sizes()][i]:
                self.board_size = [x[1] for x in self.get_default_board_sizes()][i]

        return self.board_size

    def check_settings_validity(self):
        """Checks the settings and Open Trivia DB connection validity
        with various method calls. If no Open Trivia DB categories were selected,
        a new game can be started even if the connection check returns False.

        Returns:
            True, if everything's ok, or False, if not.
        """

        return all([
            self.check_player_number_validity(),
            self.check_player_names_validity(),
            self.check_category_number_validity(),
            any([
                self.check_otdb_connection(),
                "Random (Open Trivia DB)" not in self.categories,
            ]),
        ])

    def check_player_number_validity(self):
        """Checks if enough players were added.

        Returns:
            True, if so, or False, if not.
        """

        return bool(len(self.players) > 0)

    def check_player_names_validity(self):
        """Checks if the added player names are unique.

        Returns:
            True, if so, or False, if not.
        """

        return bool(len(set(self.players)) == len(self.players))

    def check_category_number_validity(self):
        """Checks if enough categories were added.

        Returns:
            True, if so, or False, if not.
        """

        return bool(len(self.categories) >= 2)

    def check_otdb_connection(self, timeout=3):
        """Checks connection to the Open Trivia Database servers.

        Args:
            timeout (int, optional): Time in seconds after which
            a timeout-related connection error is raised. Defaults to 3.

        Returns:
            True, if the connection is ok, or False, if not.
        """

        try:
            requests.get("https://opentdb.com/", timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False

    def handle_session_save(self, players, categories, board_size):
        """Calls database class methods which ensure that no other game session is active
        and then save the current game session variables to the database.

        The difficulty is injected as an empty string value (""), as difficulty selection is
        currently not supported.

        Args:
            players (list): The selected players.
            categories (list): The selected categories.
            board_size (int): The selected board size.
        """

        self.database.remove_game_active_status()
        self.database.save_session_variables("", board_size, players, categories)

    def logout_users(self):
        """Calls a DatabaseServices class method to remove all logged in users
        (currently only one simultaneous login is allowed, but this method can handle more)."""

        return self.database.remove_logged_in_users()


settings_services = SettingsServices()
