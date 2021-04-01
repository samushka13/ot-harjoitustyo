import sqlite3

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

def create_user():
    username = input("Username: ")
    password = input("Password: ")

    db.execute("INSERT INTO Users (username, password) VALUES (?,?)", (username, password))

    print()
    print(f"Nice to meet you, {username}!")
    print()

    print("List of users on this device:")
    for user in db.execute("SELECT username FROM Users").fetchall():
        print(user['username'])
    print()
