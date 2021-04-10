from services.database_connection import db
from entities.settings import SELECT

# ------------------------------------------------
# Login operations.
# ------------------------------------------------

def add_user(username: str, password: str):
    db.execute("INSERT INTO Users (username, password) VALUES (?,?)", (username, password))

def get_credentials():
    credentials = []
    for row in db.execute("SELECT username, password FROM Users").fetchall():
        credentials.append((row['username'],row['password']))
    return credentials

def get_users():
    users = []
    for user in db.execute("SELECT username FROM Users").fetchall():
        users.append(f"{user['username']}")
    return users

def get_sorted_users():
    return '\n'.join(sorted(get_users()))

# ------------------------------------------------
# Settings & Custom Questions operations.
# ------------------------------------------------

def get_categories():
    categories = []
    for row in db.execute("SELECT category FROM Questions GROUP BY category").fetchall():
        categories.append(row['category'])
    return categories

def get_listbox_items():
    items = []
    for row in db.execute("SELECT id, category, difficulty, question, answer \
        FROM Questions").fetchall():
        row_id = row['id']
        category = row['category']
        difficulty = row['difficulty']
        question = row['question']
        answer = row['answer']
        items.append(f"{row_id}. | {category} | {difficulty} | {question} | {answer}")
    return items

def save_item_to_database(user_id: int, category: str, difficulty: str, question: str, answer: str):
    db.execute("INSERT INTO Questions (user_id, category, difficulty, question, answer) \
        VALUES (?,?,?,?,?)", (user_id, category, difficulty, question, answer))

def delete_item_from_database(question_id: int):
    db.execute(f"DELETE FROM Questions WHERE id='{question_id}'")

def delete_all_user_items_from_database():
    db.execute("DELETE FROM Questions")

def get_item_for_editing(question_id: int):
    item = db.execute(f"SELECT category, difficulty, question, answer FROM Questions \
        WHERE id='{question_id}'").fetchone()
    return item['category'], item['difficulty'], item['question'], item['answer']

def update_item(question_id: int, category: str, difficulty: str, question: str, answer: str):
    db.execute(f"UPDATE Questions SET category=?, difficulty=?, question=?, answer=? \
        WHERE id='{question_id}'", (category, difficulty, question, answer))

# These will be used to enable a feature,
# where the current user can view every user's questions (in the same database),
# but only delete (or edit) their own.
# user_id = db.execute(f"SELECT id FROM Users WHERE username='{current_user}'").fetchone()
# db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")

# ------------------------------------------------
# Game session operations.
# ------------------------------------------------

def get_category_for_player():
    return db.execute(f"SELECT category FROM Questions \
        WHERE category='{SELECT}'").fetchone()

def get_question_for_player(category: str):
    return db.execute(f"SELECT question FROM Questions \
        WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()

def get_answer_for_player(question: str):
    return db.execute(f"SELECT answer FROM Questions \
        WHERE question='{question['question']}'").fetchone()
