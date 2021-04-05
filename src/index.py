from login import LoginView
from services.database import initialize_database

def main():
    initialize_database()
    LoginView()

    # TODOS
    # ------------------------------------------------------------------
    # CUSTOM: Implement edit.
    # CUSTOM: Add filters and a search field above listbox.
    # GAME: Add die cast.
    # GAME: Add image of ouroboros.
    # GAME: Implement player turn logic.
    # GAME: replace category title and text with a legend of categories. The one in question will be somehow highlighted.
    # GAME: Fix widgets jumping when layout changes.
    # GAME: Ensure game sessions are based on game settings.
    # LOGIN: Implement error texts instead of messageboxes (create label that shows text on button command, otherwise emptystring).
    # SETTINGS: Ensure categories are updated when relevant changes are made in CustomQuestionsView.
    # GENERAL: Fix 'return' not working in certain views.
    # GENERAL: Try to make everything run in a single window that simply changes size and widgets based on current view.
    # GENERAL: Implement OpenTrivia Api stuff.
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Run all tkinter windows in the same window, only inner frames, window names and such will change.
    # GENERAL: Add 'stylings.py' where all style-related stuff should be.
    # GENERAL: Extract widgets and put them into 'widgets.py'.
    # GENERAL: Refactor everything into a sensible format (when prototyping is done).
    # GENERAL: Improve testing.
    # GENERAL: Remove unnecessary dependencies, files, etc. (Remember to save certain pieces of code elsewhere for possible later usage.)
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
