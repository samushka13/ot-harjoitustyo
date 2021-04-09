from ui.login import LoginView
from services.database_connection import initialize_database

def main():
    initialize_database()
    LoginView()

    # TODOS
    # ------------------------------------------------------------------
    # Service luo olion (esim. Question(user_id, category, difficulty, question, answer)),
    # joka menee databasehandlerin tms käsiteltäväksi.
    # Databasehandler hoitaa tiedon tallennuksen tietokantaan.

    # TESTS: MAKE AT LEAST ONE APPROPRIATE TEST!
    # GENERAL: Consider replacing all grids with places.
    # GAME: Highlight player in turn and category in question.
    # GAME: Remove bolding or decrease font size of some texts.
    # GAME: Add small icons with an appropriate color in front of player and category names.
    # GAME: Change font color of player and category names to black.
    # GAME: Add image of ouroboros.
    # GAME: Ensure game sessions are based on game settings.
    # GAME: Ensure gameview works on 'laitoksen Linuxeilla'.
    # GAME: Add close window button to 'Rules' window.
    # GAME: Add 'referee' mode where players' points can be manually altered.
    # CUSTOM: Implement edit.
    # CUSTOM: Add filters and a search field above listbox.
    # CUSTOM: Could it be possible to select many and delete them? (Edit should be disabled then.)
    # SETTINGS: Ensure categories are updated when relevant changes are made in CustomQuestionsView.
    # SETTINGS: Enable giving names to players.
    # SETTINGS: Add 'random' to category selection etc.
    # GENERAL: Try to make everything run in a single window that simply changes size and stuff.
    # GENERAL: Implement OpenTrivia Api stuff.
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Add 'stylings.py' where all style-related stuff should be.
    # GENERAL: Extract widgets and put them into 'widgets.py'.
    # GENERAL: Refactor everything into a sensible format (when prototyping is done).
    # GENERAL: Improve testing.
    # GENERAL: Remove unnecessary dependencies, files, etc.
    # (Remember to save certain pieces of code elsewhere for possible later usage.)
    # GENERAL: Ensure that the use of quotation marks '' and "" is uniform across the project.
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
