from ui.login import LoginView
from ui.game import GameView
from ui.custom_questions import CustomQuestionsView
from services.database import initialize_database
from services.create_user import create_user
from services.create_question import create_question
from services.ask_question import ask_question

def main():
    initialize_database()
    # create_user()
    # create_question()
    # ask_question()
    CustomQuestionsView()
    # LoginView()
    # GameView()

if __name__ == "__main__":
    main()
