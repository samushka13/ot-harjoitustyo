import sqlite3


db = sqlite3.connect("test.db")
db.isolation_level = None

def create_user():
    username = input("Username: ")
    password = input("Password: ")

    db.execute("INSERT INTO Users (username, password) VALUES (?,?)", (username, password))

    print("User added to database.")

    users = db.execute("SELECT username FROM Users").fetchall()
    print("List of current users:")
    print(users)

def greet_new_user(username):
    print(f"Nice to meet you, {username}!")
