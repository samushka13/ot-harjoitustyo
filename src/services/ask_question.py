import sqlite3


db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

def ask_question():
    select = input("Select category: ")
    category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()
    question = db.execute(f"SELECT question FROM Questions WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()
    answer = db.execute(f"SELECT answer FROM Questions WHERE question='{question['question']}'").fetchone()

    print()
    print(f"Question: {question['question']}")
    print()
    input("Press 'Enter' to show the correct answer.")
    print()
    print(f"Answer: {answer['answer']}")
    print()

    correct = input("Was the player's answer correct? (y/n) ")
    if correct == "y":
        print()
        print("Well done!")
        print()
    else:
        print()
        print("Better luck next time!")
        print()
