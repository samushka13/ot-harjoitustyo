from services.database_connection import db

# Login operations.

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

# Settings & Custom Questions operations.

def get_categories():
    categories = []
    for row in db.execute("SELECT category FROM Questions GROUP BY category").fetchall():
        categories.append(row['category'])
    return categories

def get_listbox_items():
    items = []
    for row in db.execute("SELECT id, category, difficulty, question, answer FROM Questions").fetchall():
        items.append(f"{row['id']}. | {row['category']} | {row['difficulty']} | {row['question']} | {row['answer']}")
    return items

def save_item_to_database(user_id: int, category: str, difficulty: str, question: str, answer: str):
    db.execute("INSERT INTO Questions (user_id, category, difficulty, question, answer) \
        VALUES (?,?,?,?,?)", (user_id, category, difficulty, question, answer))

def delete_item_from_database(question_id: int):
    db.execute(f"DELETE FROM Questions WHERE id='{question_id}'")

def delete_all_users_items_from_database():
    db.execute("DELETE FROM Questions")

# These will be used to enable a feature,
# where the current user can view every user's questions (in the same database),
# but only delete (or edit) their own.
# user_id = db.execute(f"SELECT id FROM Users WHERE username='{current_user}'").fetchone()
# db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")

# Game session operations.
