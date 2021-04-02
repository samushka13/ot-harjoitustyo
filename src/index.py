from ui.login import LoginView
from ui.game import GameView
from ui.custom_questions import CustomQuestionsView
from services.database import initialize_database
from services.create_user import create_user


def main():
    initialize_database()
    # create_user()
    CustomQuestionsView()
    LoginView()
    GameView()

    # TODO Next: Create "Play" view that has buttons that lead to "CustomQuestionsView" and "GameView".
    # TODO Next: Incorporate ask_question() to GameView.

if __name__ == "__main__":
    main()
