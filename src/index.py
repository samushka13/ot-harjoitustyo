from entities.question import Question
from entities.user import User
from entities.rules import Rules
from ui.login import LoginView
from ui.game import GameView


def placeholder_stuff():
    user = User("Samushka")
    question = Question("Computer Science", "What is 'python'?", "A programming language.")
    print(f"Hei, {user.username}!")
    print()
    print("Game settings:")
    print(Rules().rules)
    print()
    print(f"Category: {question.category}")
    print()
    print(f"Question: {question.question}")
    print()
    input("Press 'Enter' to show the correct answer.")
    print()
    print(question.answer)
    print()
    correct = input("Was the player's answer correct? (y/n) ")
    if correct == "y":
        print()
        print("Well done!")
        print()
    else:
        print()
        print("Better luck next time, dumbass.")
        print()

def main():
    placeholder_stuff()
    LoginView()
    GameView()

if __name__ == "__main__":
    main()
