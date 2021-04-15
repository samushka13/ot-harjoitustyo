# ------------------------------------------------------------------
# TODOS
# ------------------------------------------------------------------
# NEXT DL: Ensure everything works on Linux via VDI.
# ------------------------------------------------------------------
# GAME: Match token position with board categories and the category board.
# GAME: Add image of ouroboros.
# GAME: Implement points system.
# GAME: Add 'referee' mode where players' points can be manually altered.
# ------------------------------------------------------------------
# CUSTOM: Ensure that the current user can only edit their questions, not others'.
# CUSTOM: In the delete error dialog, list all users whose questions weren't deleted.
# CUSTOM: Notify if a question already exists (but give an option to still add it).
# CUSTOM: Add filters and a search field above listbox.
# CUSTOM: Add info about questions in database, such as total questions etc.
# ------------------------------------------------------------------
# SETTINGS: Enable option to include custom and/or OpenTrivia questions only.
# SETTINGS: Add 'random' to category selection etc.
# SETTINGS: Add 'randomize' (affects everything other than players).
# SETTINGS: Remember selected values when coming back from GameView or CustomContentView.
    # - This coincides with another idea that is to record all game settings for statistics.
    #   Maybe a new db table for 'game_history', with columns for each setting
    #   + user_id + status (active INTEGER, takes only values 1 or 0.)
# ------------------------------------------------------------------
# GENERAL: Move all view changes to ui from services.
# GENERAL: Implement another way for services to know what database they should be using.
# GENERAL: Improve testing (when done, remove WIP from .coveragerc).
# GENERAL: Implement config and environmental variables with .env etc.
# GENERAL: Add more classes, such as Player, Category etc.
# GENERAL: Add docstrings (and redo/double-check existing ones).
    # https://ohjelmistotekniikka-hy.github.io/python/docstring
# GENERAL: Try to make the windows and stuff a bit more responsive.
    # https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter/38809894
# GENERAL: Implement OpenTrivia API stuff.
# GENERAL: Try to make everything run in a single window that simply changes size and stuff.
# GENERAL: Implement a way to delete profile (and all questions, optionally).
# GENERAL: Implement admin login that allows to delete anyone's profile and/or questions.
# GENERAL: Remove unnecessary dependencies, files, etc.
    # - Remember to save certain pieces of code elsewhere for possible later usage.
# GENERAL: Improve UX (e.g. notify, if nothing to delete)
# ------------------------------------------------------------------
# DOCUMENTATION: Describe architecture and logic.
# DOCUMENTATION: Describe testing.
# DOCUMENTATION: Provide some kind of a manual.
# ------------------------------------------------------------------
