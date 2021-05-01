import sqlite3
from config import DATABASE_FILENAME as default_database


class DatabaseServices:
    def __init__(self, database=default_database):
        self.database = sqlite3.connect(database)
        self._initialize_database()

    def _initialize_database(self):
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

    # ------------------------------------------------
    # Login and logout operations.
    # ------------------------------------------------

    def add_user(self, username, password):
        self.database.execute("INSERT INTO Users (username, password) \
            VALUES (?,?)", (username, password))

    def get_credentials(self):
        credentials = []
        for row in self.database.execute("SELECT username, password FROM Users").fetchall():
            credentials.append((row['username'],row['password']))

        return credentials

    def get_users(self):
        users = []
        for user in self.database.execute("SELECT username FROM Users").fetchall():
            users.append(f"{user['username']}")

        return users

    def add_logged_in_user(self, username):
        self.database.execute(f"UPDATE Users SET login_status={1} \
            WHERE username='{username}'")

    def get_logged_in_user(self):
        user = []
        for row in self.database.execute(f"SELECT id, username, password FROM Users \
            WHERE login_status={1}").fetchall():
            user.append((row['id'], row['username'], row['password']))

        return user

    def remove_logged_in_users(self):
        self.database.execute(f"UPDATE Users SET login_status={0}")

    # ------------------------------------------------
    # Settings & Custom Content operations.
    # ------------------------------------------------

    def get_categories(self):
        categories = []
        for row in self.database.execute("SELECT category \
            FROM Questions GROUP BY category").fetchall():
            categories.append(row['category'])

        return categories

    def get_listbox_items(self):
        items = []
        for row in self.database.execute("SELECT * FROM Questions").fetchall():
            qid = row['id']
            cat = row['category']
            diff = row['difficulty']
            question = row['question']
            answer = row['answer']
            user = self.database.execute(f"SELECT username FROM Users \
                WHERE id='{row['user_id']}'").fetchone()
            items.append(f"{qid}. | {cat} | {diff} | {question} | {answer} ||| {user['username']}")

        return items

    def count_questions_in_the_database(self):
        total = self.database.execute("SELECT COUNT(*) FROM Questions").fetchone()

        return total['COUNT(*)']

    def get_question(self, question_id: int, user_id: int):
        total = self.database.execute(f"SELECT COUNT(*) FROM Questions \
            WHERE id='{question_id}' AND user_id='{user_id}'").fetchone()

        return total['COUNT(*)']

    def save_item_to_database(self, user_id, category, difficulty, question, answer):
        self.database.execute("INSERT INTO Questions \
            (user_id, category, difficulty, question, answer) \
            VALUES (?,?,?,?,?)", (user_id, category, difficulty, question, answer))

    def delete_item_from_database(self, question_id: int, user_id: int):
        self.database.execute(f"DELETE FROM Questions \
            WHERE id='{question_id}' AND user_id='{user_id}'")

    def delete_all_user_items_from_database(self, user_id: int):
        self.database.execute(f"DELETE FROM Questions WHERE user_id='{user_id}'")

    def get_item_for_editing(self, question_id: int):
        item = self.database.execute(f"SELECT category, difficulty, question, answer \
            FROM Questions WHERE id='{question_id}'").fetchone()

        return item['category'], item['difficulty'], item['question'], item['answer']

    def update_item(self, question_id, category, difficulty, question, answer):
        self.database.execute(f"UPDATE Questions \
            SET category=?, difficulty=?, question=?, answer=? \
            WHERE id='{question_id}'", (category, difficulty, question, answer))

    def save_session_variables(self, difficulty, size, players, categories):
        user_id = self.get_logged_in_user()[0][0]
        self.database.execute("INSERT INTO Games (user_id, active) VALUES (?,?)", (user_id, 1))
        self.database.execute(f"UPDATE Games SET difficulty='{difficulty}' WHERE active={1}")
        self.database.execute(f"UPDATE Games SET board_size='{size}' WHERE active={1}")
        for i in range(1,len(players)+1):
            self.database.execute(f"UPDATE Games SET p{i}='{players[i-1]}' WHERE active={1}")
        for i in range(1,len(categories)+1):
            self.database.execute(f"UPDATE Games SET c{i}='{categories[i-1]}' WHERE active={1}")

    # ------------------------------------------------
    # Game session operations.
    # ------------------------------------------------

    def get_session_variables(self):
        variables = self.database.execute(f"SELECT * FROM Games WHERE active={1}").fetchone()
        difficulty = variables['difficulty']
        board_size = variables['board_size']
        players = []
        for i in range(1,7):
            player = variables[f'p{i}']
            if player is not None:
                players.append(player)
        categories = []
        for i in range(1,13):
            category = variables[f'c{i}']
            if category is not None:
                categories.append(category)

        return difficulty, board_size, players, categories

    def get_question_for_player(self, category: str):
        question = self.database.execute(f"SELECT question FROM Questions \
            WHERE category='{category}' ORDER BY RANDOM()").fetchone()

        return question

    def get_answer_for_player(self, question: str):
        answer = self.database.execute(f"SELECT answer FROM Questions \
            WHERE question='{question}'").fetchone()

        return answer

    def remove_game_active_status(self):
        self.database.execute(f"UPDATE Games SET active={0} WHERE active={1}")


database_services = DatabaseServices()
