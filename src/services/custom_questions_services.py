class CustomQuestionsServices:
    """Class that describes all services related to game settings.

    Attributes:
        current_user: String value of the user's username.
    """

    def __init__(self, window, database):
        """Class constructor that creates a new settings service
        and initializes an instance of database services class.

        Args:
            current_user: String value of the user's username.
        """

        self.window = window
        self.database = database
        self.current_user = self.database.get_logged_in_users()[0][0]


    def get_item_for_editing(self, item):
        """Calls a database class method that fetches the item for editing.

        Returns:
            The result of the method call, which consists of
            four separate string values of the item, i.e.
            category, difficulty, question, and answer.
        """

        return self.database.get_item_for_editing(item)

    def update_item(self, question_id, category, difficulty, question, answer):
        """Calls a database class method that updates the item."""

        self.database.update_item(question_id, category, difficulty, question, answer)

    def get_default_difficulties(self):
        """Provides a list of default difficulty names.

        The app logic can handle adding more options,
        but the game has been designed to have only three difficulty levels.
        Therefore, changing this is not recommended.

        Returns:
            A list of the default difficulty names.
        """

        difficulty_names = [
            "Easy",
            "Intermediate",
            "Advanced Triviliast"
        ]
        return difficulty_names
