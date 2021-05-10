from repositories.database_services import database_services as default_database
from services.settings_services import settings_services


class CustomContentServices:
    """Class that describes all services related to custom content management.

    Attributes:
        database: Value of the current database.
    """

    def __init__(self, database=default_database):
        """Class constructor that initializes a new custom content service.

        Args:
            database: Value of the current database.
        """

        self.database = database

    def get_current_user_id(self):
        """Provides the id of the currently logged in user.

        Returns:
            current_user_id (int): The current user's id number.
        """

        current_user_id = self.database.get_logged_in_user()[0][0]

        return current_user_id

    def get_listbox_items(self):
        """Provides question items for the browsing listbox by calling
        a DatabaseServices class method and then formatting the items appropriately.

        Returns:
            formatted_items (list): The question items as formatted string values.
        """

        formatted_items = []
        for item in self.database.get_listbox_items():
            question_id = item[0]
            category = item[1]
            difficulty = item[2]
            question = item[3]
            answer = item[4]
            username = item[5]
            formatted_items.append(
                f"{question_id}. | {category} | {difficulty} | {question} | {answer} ||| {username}"
            )

        return formatted_items

    def get_categories(self):
        """Provides all existing categories.

        Returns:
            categories (list): The categories as string values.
        """

        categories = self.database.get_categories()

        return categories

    def get_difficulties(self):
        """Provides the game's difficulty levels.

        Returns:
            difficulties (list): The difficulties as string values.
        """

        difficulties = settings_services.get_default_difficulties()

        return difficulties

    def check_input_length_validity(self, category, question, answer):
        """Checks that the user inputs are within the set limits.

        Args:
            category (str): The content of the category input field.
            question (str): The content of the question input field.
            answer (str): The content of the answer input field.

        Returns:
            True, if input lengths are valid, and False, if they're not.
        """

        return all([
            bool("" not in (category, question, answer)),
            bool(len(category) <= 30),
            bool(len(question) <= 300),
            bool(len(answer) <= 100),
        ])

    def format_question(self, question):
        """Ensures that a question ends with a question mark.

        Args:
            question (str): The content of the question input field.

        Returns:
            question (str): The input string value appended with a question mark.
        """

        if question.endswith('?') is False:
            question += "?"

        return question

    def format_answer(self, answer):
        """Ensures that an answer ends with a dot (or an exclamation mark).

        Args:
            answer (str): The content of the answer input field.

        Returns:
            answer (str): The input string value appended with a dot.
        """

        if answer.endswith('.') is False:
            if answer.endswith('!') is False:
                answer += "."

        return answer

    def handle_save_item(self, category, difficulty, question, answer):
        """Calls a DatabaseServices class method which saves the item to database.

        Args:
            category (str): The content of the category input field.
            difficulty (str): The content of the difficulty input field.
            question (str): The content of the question input field.
            answer (str): The content of the answer input field.
        """

        self.database.save_question_item(
            self.get_current_user_id(),
            category,
            difficulty,
            self.format_question(question),
            self.format_answer(answer),
        )

    def check_owner(self, question_id):
        """Calls a DatabaseServices class method which returns either 0 or 1
        depending on whether a question with the provided ids was found,
        then checks if that integer is 1. In essence, this determines,
        whether the current user is the question's owner.

        Args:
            question_id (int): The question's id.

        Returns:
            True, if the user is the owner, False, if not.
        """

        owned = self.database.get_question_if_owned_by_user(question_id, self.get_current_user_id())

        return bool(owned == 1)

    def determine_question_ids(self, listbox):
        """Processes the string values of all listbox selections for question ids.

        Args:
            listbox (widget): The listbox widget from the UI layer.

        Returns:
            question_ids (list): The question ids as integer values.
        """

        question_ids = [listbox.get(i).split(' ', 1)[0] for i in listbox.curselection()]

        return question_ids

    def count_questions(self):
        """Calls a DatabaseServices class method which
        counts all questions in the database.

        Returns:
            questions (int): The number of question items in the database.
        """

        questions = self.database.count_questions()

        return questions

    def delete_items(self, items):
        """Calls another method to count the questions in the database
        before and after the deletion of items which, in turn, is handled
        by calling a DatabaseServices class method.

        Args:
            items (list): The question ids as integer values.

        Returns:
            before-after (int): The difference between the total number of
            questions in the database before and after the deletion operation.
        """

        before = self.count_questions()
        for item in items:
            self.database.delete_question_item(item, self.get_current_user_id())
        after = self.count_questions()

        return before-after

    def delete_all(self):
        """Calls a DatabaseServices class method which deletes all questions
        created by the current user. Also, calls another method to count the
        questions in the database before and after the deletion.

        Returns:
            before-after (int): The difference between the total number of
            questions in the database before and after the deletion operation.
        """

        before = self.count_questions()
        self.database.delete_all_user_question_items(self.get_current_user_id())
        after = self.count_questions()

        return before-after

    def get_item_for_editing(self, item):
        """Calls a DatabaseServices class method that fetches the item for editing.

        Args:
            item (int): The question's id.

        Returns:
            item (tuple): Category, difficulty, question and answer as string values.
        """

        item = self.database.get_question_item_parameters(item)

        return item

    def update_item(self, question_id, category, difficulty, question, answer):
        """Calls a database class method that updates the item.

        Args:
            question_id (int): The question item's id.
            category (str): The question item's category.
            difficulty (str): The question item's difficulty.
            question (str): The question item's question.
            answer (str): The question item's answer.
        """

        self.database.update_question_item(
            question_id,
            category,
            difficulty,
            self.format_question(question),
            self.format_answer(answer),
        )


custom_content_services = CustomContentServices()
