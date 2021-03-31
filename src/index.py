from entities.user import User
from ui.login import LoginView
from ui.game import GameView
from services.database import test_database
from services.create_user import create_user
from services.create_question import create_question
from services.ask_question import ask_question

def placeholder_stuff():
    user = User("Samushka")
    print(f"Hei, {user.username}!")

def main():
    test_database()
    create_user()
    create_question()
    ask_question()
    LoginView()
    GameView()

if __name__ == "__main__":
    main()
