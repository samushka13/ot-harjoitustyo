import sqlite3

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

def create_question():
    user_id = 1
    category = input("Category: ")
    question = input("Question: ")
    answer = input("Answer: ")

    db.execute("INSERT INTO Questions (user_id, category, question, answer) VALUES (?,?,?,?)", (user_id, category, question, answer))

    print()
    print("Question added to your database.")
    print()

    print("Here's a list of all questions in the database:")

    for row in db.execute("SELECT category, question, answer FROM Questions").fetchall():
        print(f"Category: {row['category']}")
        print(f"Question: {row['question']}")
        print(f"Answer: {row['answer']}")
        print()

    remove = input("Do you wish to delete all your questions? (y/n) ")

    if remove == "y":
        user_id = db.execute("SELECT id FROM Users WHERE username='samushka'").fetchone()
        db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")
        print("Your questions have been deleted.")
        print()
    else:
        print("Your questions are safe.")
        print()
