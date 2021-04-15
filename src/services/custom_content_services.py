class CustomContentServices:
    """Class that describes all services related to game settings.

    Attributes:
        current_user: String value of the user's username.
        database: Value of the current database.
    """

    def __init__(self, window, database):
        """Class constructor that creates a new settings service
        and initializes an instance of database services class.

        Args:
            current_user: String value of the user's username.
            database: Value of the current database.
        """

        self.window = window
        self.database = database
        self.current_user_id = self.get_current_user_id()
        self.current_username = self.get_current_username()

    def get_listbox_items(self):
        """Calls DatabaseServices class method to get items.

        Returns:
            A list of preformatted string values describing question items.
        """

        return self.database.get_listbox_items()

    def get_categories(self):
        """Calls DatabaseServices class method to get categories.

        Returns:
            A list of string values describing categories.
        """

        return self.database.get_categories()

    def get_difficulties(self):
        """Calls SettingsServices class method to get difficulties for the combobox.

        Returns:
            A list of string values describing difficulties.
        """

        from services.settings_services import SettingsServices

        return SettingsServices(self.window, self.database).get_default_difficulties()

    def get_current_user_id(self):
        """Calls DatabaseServices class method to get the currently logged in user's id.

        Returns:
            An integer value describing the user's id.
        """

        return self.database.get_logged_in_users()[0][0]

    def get_current_username(self):
        """Calls DatabaseServices class method to get the currently logged in user's username.

        Returns:
            A string value describing the user's username.
        """

        return self.database.get_logged_in_users()[0][1]

    def check_input_validity(self, category, difficulty, question, answer):
        """Checks that the user input contains no empty values.

        Args:
            category: A string value describing a category.
            difficulty: A string value describing a difficulty.
            question: A string value describing a question.
            answer: A string value describing an answer.

        Returns:
            True, if inputs are valid, and False, if they're not.
        """

        return bool("" not in (category, difficulty, question, answer))

    def format_question(self, question):
        """Ensures that a question has a question mark.

        Args:
            question: A string value describing a question.

        Returns:
            The input string value appended with a question mark.
        """

        if question.endswith('?') is False:
            question = question + "?"
        return question

    def format_answer(self, answer):
        """Ensures that an answer ends with a dot or an exclamation mark.

        Args:
            answer: A string value describing an answer.

        Returns:
            The input string value appended with a dot.
        """

        if answer.endswith('.') is False:
            if answer.endswith('!') is False:
                answer = answer + "."
        return answer

    def handle_save_item(self, category, difficulty, question, answer):
        """Calls a DatabaseServices class method which saves the item to database.

        Args:
            category: A string value describing a category.
            difficulty: A string value describing a difficulty.
            question: A string value describing a question.
            answer: A string value describing an answer.
        """

        self.database.save_item_to_database(
            self.current_user_id,
            category,
            difficulty,
            self.format_question(question),
            self.format_answer(answer),
        )

    def check_owner(self, question_id):
        """Calls a DatabaseServices class method which returns an integer (0 or 1),
        then checks if that integer is 1. In essence, this determines,
        whether the current user is the question's owner.

        Args:
            question_id: An integer value describing a question's id.

        Returns:
            True, if the user is the owner, False, if not.
        """

        return bool(self.database.get_question(question_id, self.current_user_id) == 1)

    def determine_question_ids(self, listbox):
        """Processes the string values of all listbox selections for question ids.

        Args:
            listbox: A value describing the listbox from the UI.

        Returns:
            A list of question ids.
        """

        return [listbox.get(i).split(' ', 1)[0] for i in listbox.curselection()]

    def count_questions(self):
        """Calls a DatabaseServices class method which
        counts all questions in the database.

        Returns:
            An integer describing the number of question items in the database.
        """

        return self.database.count_questions_in_the_database()

    def delete_items(self, items):
        """Calls the above method to count the questions in the database
        before and after the deletion of items which, in turn, is handled
        by calling a DatabaseServices class method.

        Args:
            items: A list of question ids.

        Returns:
            An integer describing the difference between
            total number of questions in the database
            before and after the deletion operation.
        """

        before = self.count_questions()
        for item in items:
            self.database.delete_item_from_database(item, self.current_user_id)
        after = self.count_questions()
        return before-after

    def delete_all(self):
        """Calls a DatabaseServices class method which deletes
        all questions created by the current user."""

        self.database.delete_all_user_items_from_database(self.current_user_id)

    def get_item_for_editing(self, item):
        """Calls a DatabaseServices class method that fetches the item for editing.

        Args:
            item: An integer describing the question's id.

        Returns:
            Four separate string values of the question item, i.e.
            category, difficulty, question, and answer.
        """

        return self.database.get_item_for_editing(item)

    def update_item(self, question_id, category, difficulty, question, answer):
        """Calls a database class method that updates the item.

        Args:
            question_id: An integer describing a question's id.
            category: A string value describing a category.
            difficulty: A string value describing a difficulty.
            question: A string value describing a question.
            answer: A string value describing an answer.
        """

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
