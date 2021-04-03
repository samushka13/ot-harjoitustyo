import sqlite3


db = sqlite3.connect("test.db")
db.isolation_level = None

def get_database_connection():
    return db

def create_users_table():
    db.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

def create_questions_table():
    db.execute("CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES Users, category TEXT, difficulty TEXT, question TEXT, answer TEXT)")

def initialize_database():
    get_database_connection()
    create_users_table()
    create_questions_table()
