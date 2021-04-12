from services.database_services import DatabaseServices, DATABASE_FILENAME
from ui.login import LoginView

def main():
    database = DatabaseServices(DATABASE_FILENAME)
    LoginView(database)

    # ------------------------------------------------------------------
    # TODOS
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
    # SETTINGS: Add 'randomize' (affects everything other than players).
    # SETTINGS: Remember selected values when coming back from GameView or CustomQuestionsView.
    # ------------------------------------------------------------------
    # GENERAL: Refactor everything into a sensible format when prototyping is done.
    # GENERAL: Add more classes, such as Player, Category etc.
    # GENERAL: Improve testing.
    # GENERAL: Implement a way to get the current user (now it's just passed on).
    # GENERAL: Implement logout in settings (and return to login screen afterwards).
    # GENERAL: Implement OpenTrivia API stuff.
    # GENERAL: Consider replacing all grids with places.
    # GENERAL: Try to make everything run in a single window that simply changes size and stuff.
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Remove unnecessary dependencies, files, etc.
    # (Remember to save certain pieces of code elsewhere for possible later usage.)
    # GENERAL: Ensure that the use of quotation marks '' and "" is uniform across the project.
    # GENERAL: Enable configurations, such as .db file naming.
    # ------------------------------------------------------------------
    # DOCUMENTATION: Describe architecture and logic.
    # DOCUMENTATION: Describe testing.
    # DOCUMENTATION: Provide some kind of a manual.
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
