import sqlite3

DATABASE_FILENAME = "test.db"
db = sqlite3.connect(DATABASE_FILENAME)

def get_database_connection():
    db.isolation_level = None
    db.row_factory = sqlite3.Row
    return db

def create_users_table():
    db.execute("CREATE TABLE IF NOT EXISTS Users \
        (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

def create_questions_table():
    db.execute("CREATE TABLE IF NOT EXISTS Questions \
        (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES Users, \
        category TEXT, difficulty TEXT, question TEXT, answer TEXT)")

def initialize_database():
    get_database_connection()
    create_users_table()
    create_questions_table()
