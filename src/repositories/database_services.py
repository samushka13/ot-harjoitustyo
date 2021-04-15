import sqlite3

class DatabaseServices:
    def __init__(self, database_name):
        self.database = sqlite3.connect(database_name, timeout=10)
        self.initialize_database()

    def initialize_database(self):
        self.database.isolation_level = None
        self.database.row_factory = sqlite3.Row

        self.database.execute("CREATE TABLE IF NOT EXISTS Users \
            (id INTEGER PRIMARY KEY, username TEXT, password TEXT, login_status INTEGER)")

        self.database.execute("CREATE TABLE IF NOT EXISTS Questions \
            (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES Users, \
            category TEXT, difficulty TEXT, question TEXT, answer TEXT)")

        return self.database

    # ------------------------------------------------
    # Login operations.
    # ------------------------------------------------

    def add_user(self, user):
        self.database.execute("INSERT INTO Users (username, password) \
            VALUES (?,?)", (user.username, user.password))
        return (user.username, user.password)

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

    def get_sorted_users(self):
        return '\n'.join(sorted(self.get_users()))

    def add_logged_in_user(self, username):
        self.database.execute(f"UPDATE Users SET login_status={1} \
            WHERE username='{username}'")

    def get_logged_in_users(self):
        credentials = []
        for row in self.database.execute(f"SELECT username, password FROM Users \
            WHERE login_status={1}").fetchall():
            credentials.append((row['username'],row['password']))
        return credentials

    # ------------------------------------------------
    # Logout operations.
    # ------------------------------------------------

    def remove_logged_in_users(self):
        self.database.execute(f"UPDATE Users SET login_status={0}")

    # ------------------------------------------------
    # Settings & Custom Questions operations.
    # ------------------------------------------------

    def get_categories(self):
        categories = []
        for row in self.database.execute("SELECT category \
            FROM Questions GROUP BY category").fetchall():
            categories.append(row['category'])
        return categories

    def get_listbox_items(self):
        items = []
        for row in self.database.execute("SELECT id, category, difficulty, question, answer \
            FROM Questions").fetchall():
            row_id = row['id']
            category = row['category']
            difficulty = row['difficulty']
            question = row['question']
            answer = row['answer']
            items.append(f"{row_id}. | {category} | {difficulty} | {question} | {answer}")
        return items

    def save_item_to_database(self, user_id, category, difficulty, question, answer):
        self.database.execute("INSERT INTO Questions \
            (user_id, category, difficulty, question, answer) \
            VALUES (?,?,?,?,?)", (user_id, category, difficulty, question, answer))

    def delete_item_from_database(self, question_id: int):
        self.database.execute(f"DELETE FROM Questions WHERE id='{question_id}'")

    def delete_all_user_items_from_database(self):
        self.database.execute("DELETE FROM Questions")

    def get_item_for_editing(self, question_id: int):
        item = self.database.execute(f"SELECT category, difficulty, question, answer \
            FROM Questions WHERE id='{question_id}'").fetchone()
        return item['category'], item['difficulty'], item['question'], item['answer']

    def update_item(self, question_id, category, difficulty, question, answer):
        self.database.execute(f"UPDATE Questions \
            SET category=?, difficulty=?, question=?, answer=? \
            WHERE id='{question_id}'", (category, difficulty, question, answer))

    # These will be used to enable a feature,
    # where the current user can view every user's questions (in the same database),
    # but only delete (or edit) their own.
    # user_id = db.execute(f"SELECT id FROM Users WHERE username='{current_user}'").fetchone()
    # db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")

    # ------------------------------------------------
    # Game session operations.
    # ------------------------------------------------

    def get_category_for_player(self, category: str):
        return self.database.execute(f"SELECT category FROM Questions \
            WHERE category='{category}'").fetchone()

    def get_question_for_player(self, category: str):
        return self.database.execute(f"SELECT question FROM Questions \
            WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()

    def get_answer_for_player(self, question: str):
        return self.database.execute(f"SELECT answer FROM Questions \
            WHERE question='{question['question']}'").fetchone()