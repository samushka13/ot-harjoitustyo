from ui.login import LoginView
from ui.board import GameView
from ui.custom_questions import CustomQuestionsView
from services.database import initialize_database


def main():
    initialize_database()
    LoginView()
    # SettingsView()
    CustomQuestionsView()
    GameView()

    # TODOS:
    # Create "SettingsView" that has buttons leading to "CustomQuestionsView" and "GameView".
    # Incorporate ask_question() to 'GameView'.
    # Decide the default board size.
    # Add die (or dice on higher difficulties) to 'GameView'.
    # Error-texts to login instead of messageboxes (create label that shows text on button command, otherwise emptystring).
    # Clear-button to login.
    # In GameView: replace category title and text with a legend of categories. The one in question will be somehow highlighted.
    # Add password entry field to login.
    # Implement OpenTrivia Api stuff.
    # Run all tkinter windows in the same window, only inner frames, window names and such will change.
    # Add 'stylings.py' where all style-related stuff should be.
    # Extract widgets and put them into 'widgets.py'.
    # Refactor everything (when prototyping is done).
    # Improve testing.

if __name__ == "__main__":
    main()
