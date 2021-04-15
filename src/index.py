from repositories.database_services import DatabaseServices
from ui.login_view import LoginView
from config import DATABASE_FILENAME

def main():
    database = DatabaseServices(DATABASE_FILENAME)
    LoginView(database)

    # ------------------------------------------------------------------
    # TODOS
    # ------------------------------------------------------------------
    # NEXT DL: Move all view changes to ui from services.
    # NEXT DL: Refactor all code that is included in the release.
    # NEXT DL: Isolate/mark all WIP stuff and crappy code clearly.
    # NEXT DL: Ohjelman alustava rakenne luokka- ja pakkauskaaviona:
        # - ks. https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/dokumentaatio/arkkitehtuuri.md
        # - ks. https://ohjelmistotekniikka-hy.github.io/python/materiaali#pakkauskaavio
        # - sovelluslogiikan kannalta oleelliset luokat
        # - sovelluksen pakkausrakenne
        # - lisää repoon dokumentaatio/arkkitehtuuri.md:
        #   -> upota kaaviot kuvina tiedostoon (kirjoita myös juttuja auki)
        #   -> linkki tiedostoon README:stä
    # NEXT DL: Ensure everything works on Linux via VDI.
    # NEXT DL: Check pylint score is higher than 7.00.
    # ------------------------------------------------------------------
    # GAME: Match token position with board categories and the category board.
    # GAME: Add image of ouroboros.
    # GAME: Implement points system.
    # GAME: Add 'referee' mode where players' points can be manually altered.
    # ------------------------------------------------------------------
    # CUSTOM: Ensure that the current user can only edit/delete their questions, not others'.
    # CUSTOM: Notify if a question already exists (but give an option to still add it).
    # CUSTOM: Add filters and a search field above listbox.
    # CUSTOM: Add info about questions in database, such as total questions etc.
    # ------------------------------------------------------------------
    # SETTINGS: Enable option to include custom and/or OpenTrivia questions only.
    # SETTINGS: Add 'random' to category selection etc.
    # SETTINGS: Add 'randomize' (affects everything other than players).
    # SETTINGS: Remember selected values when coming back from GameView or CustomQuestionsView.
        # - This coincides with another idea that is to record all game settings for statistics.
        #   Maybe a new db table for games started, with columns for each setting
        #   + status (active INTEGER, takes only values 1 or 0.)
    # ------------------------------------------------------------------
    # GENERAL: Implement environmental variables with .env etc.
    # GENERAL: Refactor everything into a sensible format when prototyping is done.
    # GENERAL: Add more classes, such as Player, Category etc.
    # GENERAL: Improve testing.
    # GENERAL: Add docstrings (and double-check existing ones).
        # -> https://ohjelmistotekniikka-hy.github.io/python/docstring
    # GENERAL: Try to make the windows and stuff a bit more responsive.
        # -> https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter/38809894
    # GENERAL: Implement a way to get the current user (now it's just passed on).
    # GENERAL: Implement logout in settings (and return to login screen afterwards).
    # GENERAL: Implement OpenTrivia API stuff.
    # GENERAL: Try to make everything run in a single window that simply changes size and stuff.
    # GENERAL: Implement a way to delete profile (and all questions, optionally).
    # GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
    # GENERAL: Remove unnecessary dependencies, files, etc.
        # - Remember to save certain pieces of code elsewhere for possible later usage.
    # GENERAL: Ensure that the use of quotation marks '' and "" is uniform across the project.
    # GENERAL: Enable configurations, such as .db file naming.
    # ------------------------------------------------------------------
    # DOCUMENTATION: Describe architecture and logic.
    # DOCUMENTATION: Describe testing.
    # DOCUMENTATION: Provide some kind of a manual.
    # ------------------------------------------------------------------

if __name__ == "__main__":
    main()
