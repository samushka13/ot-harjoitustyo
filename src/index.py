from ui.login import LoginView
from services.database_connection import initialize_database

def main():
    initialize_database()
    LoginView()

    # ------------------------------------------------------------------
    # TODOS
    # ------------------------------------------------------------------
    # CRITICAL: IMPLEMENT AT LEAST ONE APPROPRIATE TEST!
    # CRITICAL: Ensure stuff works on 'laitoksen Linuxeilla'!
    # CRITICAL: Include notes where things are still WIP!
    # CRITICAL: Remove certain WIPs before next deadline!
    # ------------------------------------------------------------------
    # GAME: Match token position with board categories and the category board.
    # GAME: Add image of ouroboros.
    # GAME: Implement points system.
    # GAME: Add 'referee' mode where players' points can be manually altered.
    # ------------------------------------------------------------------
    # CUSTOM: Add filters and a search field above listbox.
    # ------------------------------------------------------------------
    # SETTINGS: Enable choosing to include custom and/or OpenTrivia questions only.
    # SETTINGS: Add 'random' to category selection etc.
    # SETTINGS: Remember selected values when coming back from GameView or CustomQuestionsView.
    # ------------------------------------------------------------------
    # GENERAL: Implement OpenTrivia Api stuff.
    # GENERAL: Try to make everything run in a single window that simply changes size and stuff.
    # (If not, remove resize_window.py under services.)
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Consider replacing all grids with places.
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Refactor everything into a sensible format (when prototyping is done).
    # GENERAL: Improve testing.
    # GENERAL: Remove unnecessary dependencies, files, etc.
    # (Remember to save certain pieces of code elsewhere for possible later usage.)
    # GENERAL: Ensure that the use of quotation marks '' and "" is uniform across the project.
    # GENERAL: Enable configurations, such as .db file naming.
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
