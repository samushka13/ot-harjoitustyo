from services.database_connection import initialize_database
from ui.login import LoginView

def main():
    initialize_database()
    LoginView()

    # ------------------------------------------------------------------
    # TODOS
    # ------------------------------------------------------------------
    # CRITICAL: Only include login (and questions) to the 13.4. DL,
    # as they are the only functionalities that work well enough.
    # -> Therefore, focus on the classes and tests of these functionalities.
    # CRITICAL: IMPLEMENT APPROPRIATE TESTS! (E.g. User/Question class select, insert, update...)
    # CRITICAL: Ensure stuff works on 'laitoksen Linuxeilla'! (check python version at least)
    # CRITICAL: Include notes where things are still WIP!
    # CRITICAL: Add more classes, such as Player, Category etc.
    # ------------------------------------------------------------------
    # GAME: Match token position with board categories and the category board.
    # GAME: Add image of ouroboros.
    # GAME: Implement points system.
    # GAME: Add 'referee' mode where players' points can be manually altered.
    # ------------------------------------------------------------------
    # CUSTOM: Add filters and a search field above listbox.
    # CUSTOM: Add info about questions in database, such as total questions etc.
    # ------------------------------------------------------------------
    # SETTINGS: Enable option to include custom and/or OpenTrivia questions only.
    # SETTINGS: Add 'random' to category selection etc.
    # SETTINGS: Remember selected values when coming back from GameView or CustomQuestionsView.
    # ------------------------------------------------------------------
    # GENERAL: Implement a way to get the current user.
    # GENERAL: Implement logout in settings (and return to login screen afterwards).
    # GENERAL: Implement OpenTrivia Api stuff.
    # GENERAL: Consider replacing all grids with places.
    # GENERAL: Try to make everything run in a single window that simply changes size and stuff.
    # (If not, remove resize_window.py under services.)
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
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
