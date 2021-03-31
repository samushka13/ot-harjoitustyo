import sqlite3


db = sqlite3.connect("test.db")
db.isolation_level = None

def create_question():
    user_id = 1
    category = input("Category: ")
    question = input("Question: ")
    answer = input("Answer: ")

    db.execute("INSERT INTO Questions (user_id, category, question, answer) VALUES (?,?,?,?)", (user_id, category, question, answer))

    print("Question added to your database.")

    questions = db.execute("SELECT category, question, answer FROM Questions").fetchall()
    print(questions)

    remove = input("Do you wish to delete all your questions? (y/n) ")

    if remove == "y":
        db.execute("DELETE FROM Questions WHERE user_id = 1")
        print("Your questions have been deleted.")
    else:
        print("Your questions are safe.")
