from login import LoginView
from services.database import initialize_database

def main():
    initialize_database()
    LoginView()

    # TODOS
    # ------------------------------------------------------------------
    # CUSTOM: Implement edit.
    # CUSTOM: Add filters and a search field above listbox.
    # GAME: Add image of ouroboros.
    # GAME: Implement player turn and movement logic.
    # GAME: Ensure game sessions are based on game settings.
    # GAME: Ensure gameview works on 'laitoksen Linuxeilla'.
    # GAME: Add 'referee' mode where players' points can be manually altered in case of mistakes were made.
    # LOGIN: Implement error texts instead of messageboxes (create label that shows text on button command, otherwise emptystring).
    # SETTINGS: Ensure categories are updated when relevant changes are made in CustomQuestionsView.
    # GENERAL: Try to make everything run in a single window that simply changes size and widgets based on current view.
    # GENERAL: Implement OpenTrivia Api stuff.
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Add 'stylings.py' where all style-related stuff should be.
    # GENERAL: Extract widgets and put them into 'widgets.py'.
    # GENERAL: Refactor everything into a sensible format (when prototyping is done).
    # GENERAL: Improve testing.
    # GENERAL: Remove unnecessary dependencies, files, etc. (Remember to save certain pieces of code elsewhere for possible later usage.)
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
