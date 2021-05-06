import sqlite3
from config import DATABASE_FILENAME as default_database


class DatabaseServices:
    """Class that describes all database-related services.

    Attributes:
        database: The current database. Defaults to default_database.
    """

    def __init__(self, database=default_database):
        """Class constructor that initializes a new database service.

        Args:
            database: The current database. Defaults to default_database.
        """

        self.database = sqlite3.connect(database)
        self._initialize_database()

    def _initialize_database(self):
        """Assigns the isolation level and sets up the database
        with appropriate tables if they do not already exits.

        Returns:
            self.database (database): The current database.
        """

        self.database.isolation_level = None
        self.database.row_factory = sqlite3.Row

        self.database.execute("CREATE TABLE IF NOT EXISTS Users \
            (id INTEGER PRIMARY KEY, username TEXT, password TEXT, login_status INTEGER)")

        self.database.execute("CREATE TABLE IF NOT EXISTS Questions \
            (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES Users, \
            category TEXT, difficulty TEXT, question TEXT, answer TEXT)")

        self.database.execute("CREATE TABLE IF NOT EXISTS Games \
            (id INTEGER PRIMARY KEY, active INTEGER, user_id INTEGER REFERENCES Users, \
            difficulty TEXT, board_size INTEGER, \
            p1 TEXT, p2 TEXT, p3 TEXT, p4 TEXT, p5 TEXT, p6 TEXT, \
            c1 TEXT, c2 TEXT, c3 TEXT, c4 TEXT, c5 TEXT, c6 TEXT, \
            c7 TEXT, c8 TEXT, c9 TEXT, c10 TEXT, c11 TEXT, c12 TEXT)")

        return self.database

    # ----------------------------------------------------------------------------------------
    # Login and logout operations.
    # ----------------------------------------------------------------------------------------

    def add_user(self, username, password):
        """Inserts a new user with the provided parameters.

        Args:
            username (str): The new user's username.
            password (str): The new user's password.
        """

        self.database.execute("INSERT INTO Users (username, password) \
            VALUES (?,?)", (username, password))

    def get_credentials(self):
        """Selects all user credentials and appends them to an empty list.

        Returns:
            credentials (list): Credentials as tuples of (username, password).
        """

        credentials = []
        for row in self.database.execute("SELECT username, password FROM Users").fetchall():
            credentials.append((row['username'],row['password']))

        return credentials

    def get_users(self):
        """Selects all usernames and appends them to an empty list.

        Returns:
            users (list): Usernames as string values.
        """

        users = []
        for user in self.database.execute("SELECT username FROM Users").fetchall():
            users.append(f"{user['username']}")

        return users

    def add_logged_in_user(self, username):
        """Sets the current user's status as 'logged in'.

        Args:
            username (str): The current user's username.
        """

        self.database.execute(f"UPDATE Users SET login_status={1} \
            WHERE username='{username}'")

    def get_logged_in_user(self):
        """Selects the logged in users and appends them to an empty list.

        The app logic can currently handle only one simultaneous login,
        but this method can accommodate multiple.

        Returns:
            users (list): Users as tuples of (id, username, password).
        """

        users = []
        for row in self.database.execute(f"SELECT id, username, password FROM Users \
            WHERE login_status={1}").fetchall():
            users.append((row['id'], row['username'], row['password']))

        return users

    def remove_logged_in_users(self):
        """Sets all users as logged out."""

        self.database.execute(f"UPDATE Users SET login_status={0}")

    # ----------------------------------------------------------------------------------------
    # Settings & Custom Content operations.
    # ----------------------------------------------------------------------------------------

    def get_categories(self):
        """Selects all categories and appends them to an empty list.

        Returns:
            categories (list): Categories as string values.
        """

        categories = []
        for row in self.database.execute("SELECT category \
            FROM Questions GROUP BY category").fetchall():
            categories.append(row['category'])

        return categories

    def get_listbox_items(self):
        """Selects all question items and appends them to an empty list.

        Returns:
            items (list): Question items as tuples of string values.
        """

        items = []
        for row in self.database.execute("SELECT * FROM Questions").fetchall():
            user = self.database.execute(f"SELECT username FROM Users \
                WHERE id='{row['user_id']}'").fetchone()
            items.append((
                row['id'],
                row['category'],
                row['difficulty'],
                row['question'],
                row['answer'],
                user['username']
            ))

        return items

    def count_questions(self):
        """Selects the total count of existing question items.

        Returns:
            questions (int): The total number of questions.
        """

        total = self.database.execute("SELECT COUNT(*) FROM Questions").fetchone()
        questions = total['COUNT(*)']

        return questions

    def get_question_if_owned_by_user(self, question_id: int, user_id: int):
        """Selects the question that matches the provided parameters.

        Args:
            question_id (int): The question item's id.
            user_id (int): The user's id.

        Returns:
            owned (int): The count of owned questions (either 0 or 1).
        """

        question = self.database.execute(f"SELECT COUNT(*) FROM Questions \
            WHERE id='{question_id}' AND user_id='{user_id}'").fetchone()
        owned = question['COUNT(*)']

        return owned

    def save_question_item(self, user_id, category, difficulty, question, answer):
        """Inserts a new question item with the provided parameters.

        Args:
            user_id (int): The user's id.
            category (str): The question item's category.
            difficulty (str): The question item's difficulty.
            question (str): The question item's question.
            answer (str): The question item's answer.
        """

        self.database.execute("INSERT INTO Questions \
            (user_id, category, difficulty, question, answer) \
            VALUES (?,?,?,?,?)", (user_id, category, difficulty, question, answer))

    def delete_question_item(self, question_id: int, user_id: int):
        """Deletes the question item that matches the provided parameters.

        Args:
            question_id (int): The question item's id.
            user_id (int): The user's id.
        """

        self.database.execute(f"DELETE FROM Questions \
            WHERE id='{question_id}' AND user_id='{user_id}'")

    def delete_all_user_question_items(self, user_id: int):
        """Deletes all questions that belong to the current user.

        Args:
            user_id (int): The user's id.
        """

        self.database.execute(f"DELETE FROM Questions WHERE user_id='{user_id}'")

    def get_question_item_parameters(self, question_id: int):
        """Selects the question item that matches the provided parameter.

        Args:
            question_id (int): The question item's id.

        Returns:
            item_parameters (tuple): Category, difficulty, question and answer as string values.
        """

        item = self.database.execute(f"SELECT category, difficulty, question, answer \
            FROM Questions WHERE id='{question_id}'").fetchone()
        item_parameters = (item['category'], item['difficulty'], item['question'], item['answer'])

        return item_parameters

    def update_question_item(self, question_id, category, difficulty, question, answer):
        """Updates the question item based on the provided parameters.

        Args:
            question_id (int): The question item's id.
            category (str): The question item's category.
            difficulty (str): The question item's difficulty.
            question (str): The question item's question.
            answer (str): The question item's answer.
        """

        self.database.execute(f"UPDATE Questions \
            SET category=?, difficulty=?, question=?, answer=? \
            WHERE id='{question_id}'", (category, difficulty, question, answer))

    def save_session_variables(self, difficulty, board_size, players, categories):
        """Inserts a new game item into the database as active and then
        updates other attributes based on the provided parameters.

        Args:
            difficulty (str): The name of the selected difficulty.
            board_size (int): The board selected size.
            players (list): The selected players.
            categories (list): The selected categories.
        """

        user_id = self.get_logged_in_user()[0][0]
        self.database.execute("INSERT INTO Games (user_id, active) VALUES (?,?)", (user_id, 1))
        self.database.execute(f"UPDATE Games SET difficulty='{difficulty}' WHERE active={1}")
        self.database.execute(f"UPDATE Games SET board_size='{board_size}' WHERE active={1}")
        for i in range(1,len(players)+1):
            self.database.execute(f"UPDATE Games SET p{i}='{players[i-1]}' WHERE active={1}")
        for i in range(1,len(categories)+1):
            self.database.execute(f"UPDATE Games SET c{i}='{categories[i-1]}' WHERE active={1}")

    # ----------------------------------------------------------------------------------------
    # Game session operations.
    # ----------------------------------------------------------------------------------------

    def get_session_variables(self):
        """Selects the game session variables of the currently active game.

        Returns:
            session (tuple): (dfficulty (str), board size (str), players (list), categories (list)).
        """

        game = self.database.execute(f"SELECT * FROM Games WHERE active={1}").fetchone()
        players = []
        for i in range(1,7):
            player = game[f'p{i}']
            if player is not None:
                players.append(player)
        categories = []
        for i in range(1,13):
            category = game[f'c{i}']
            if category is not None:
                categories.append(category)

        session = (game['difficulty'], game['board_size'], players, categories)

        return session

    def get_question_for_player(self, category: str):
        """Selects a random question item based on the selected category.

        Args:
            category (str): The current category.

        Returns:
            question (str): The question from the current category.
        """

        question = self.database.execute(f"SELECT question FROM Questions \
            WHERE category='{category}' ORDER BY RANDOM()").fetchone()

        return question['question']

    def get_answer_for_player(self, question: str):
        """Selects a random question item based on the selected category.

        Args:
            question (str): The current question.

        Returns:
            answer (str): The answer to the current question.
        """

        answer = self.database.execute(f"SELECT answer FROM Questions \
            WHERE question='{question}'").fetchone()

        return answer['answer']

    def remove_game_active_status(self):
        """Inactivates all game items."""

        self.database.execute(f"UPDATE Games SET active={0} WHERE active={1}")


database_services = DatabaseServices()
