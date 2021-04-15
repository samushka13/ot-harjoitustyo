from tkinter import messagebox

# ------------------------------------------------------
# "What's new in this version?"
# ------------------------------------------------------

def whats_new_dialog():
    return messagebox.showinfo(
        "What's new",

"""These are currently working:

- All login-related stuff (tests 100 %).
- All settings-related stuff (tests 100 %).
- All stuff related to custom content (no tests yet).
- All database-related stuff (no tests yet).

Also, the repository has been cleaned up from last week, \
and all work in progress has been moved to the WIP folder. \
The WIP files are basically prototypes of various functionalities, \
and the code included is quite poor. Therefore, they should not be reviewed.

What to expect next week?

- Tests for custom content services.
- A game board view that is based on the selected settings. \
(game progression-related functionalities will be introduced later)

""",
    )

def show_game_not_ready_dialog():
    return messagebox.showinfo(
        "Not yet accessible",
"The game view creation logic isn't quite ready yet, \
so it has been excluded from this release. \
It will be included in next week's release, in some form, at least.",
    )

# ------------------------------------------------------
# LoginView dialogs.
# ------------------------------------------------------

def show_invalid_username_dialog():
    return messagebox.showinfo(
        "Invalid Username",
        "Username should be 3 or more characters long.",
    )

def show_login_error_dialog():
    return messagebox.showinfo(
        "Login Error",
        "Username and password don't match.",
    )

def show_login_success_dialog(username: str):
    return messagebox.showinfo(
        "Logged in!",
        f"Welcome back, {username}!",
    )

def show_username_created_dialog(username: str):
    return messagebox.showinfo(
        "Username Created",
        f"Nice to meet you, {username}!",
    )

def show_registration_error_dialog():
    return messagebox.showinfo(
        "Registration Error",
        "There was a problem with registering your credentials. Please try again.\
        \n\nIf the problem persists, try reinstalling the software.",
    )

def show_users_dialog(users):
    return messagebox.showinfo(
            "Users",
            f"List of users on this device: \n\n{users}",
        )

def show_no_users_dialog():
    return messagebox.showinfo(
            "Users",
            "There are currently no users on this device.",
        )

# ------------------------------------------------------
# SettingsView dialogs.
# ------------------------------------------------------

def show_player_number_error_dialog():
    return messagebox.showinfo(
        "No players added",
        "At least one player must be added to start a new game.\
        \n\nYou can type in a custom name or select one from predefined values.\n"
    )

def show_player_name_error_dialog():
    return messagebox.showinfo(
        "Player name error",
        "Players must be given unique names."
    )

def show_category_number_error_dialog():
    return messagebox.showinfo(
        "Not enough categories",
        "At least two categories must be added to start a new game.\
        \n\nYou can select them using the category dropdown lists.\
        \n\nIf the lists are empty, try creating some questions in the Custom Content view.\n"
    )

# ------------------------------------------------------
# CustomContentView dialogs.
# ------------------------------------------------------

def show_save_error_dialog():
    return messagebox.showinfo(
        "Save Error",
        "Ensure that all fields have text in them."
    )

def show_save_successful_dialog():
    return messagebox.showinfo(
        "Hooray!",
        "Question saved successfully. \
         \n\nCreate more to improve the gaming experience.\n"
    )

def show_edit_error_dialog():
    return messagebox.showinfo(
        "Edit Error",
        "This question doesn't seem to belong to you. \
         \n\nAsk another user or an admin user to edit this question.\n"
    )

def show_delete_confirmation_dialog(number: int):
    if number == 1:
        dialog = messagebox.askquestion(
            "Delete Item",
            "Are you sure you want to delete the selected question?"
        )
    else:
        dialog = messagebox.askquestion(
            "Delete Items",
            f"Are you sure you want to delete these {number} selected questions?"
        )
    return dialog

def show_delete_error_dialog(number: int):
    if number == 1:
        dialog = messagebox.showinfo(
        "Delete Error",
        f"{number} questions were not deleted, as they belong to a different username. \
        \n\nAsk another user or an admin user to delete these questions.\n"
    )
    else:
        dialog = messagebox.showinfo(
        "Delete Error",
        f"{number} questions were not deleted, as they belong to different usernames. \
        \n\nAsk other users or an admin user to delete these questions.\n"
    )
    return dialog

def show_delete_all_confirmation_dialog():
    return messagebox.askquestion(
        "Delete All",
        "Are you sure you want to delete all your questions? \
        \n\nQuestions created by others will remain.\n"
    )

# ------------------------------------------------------
# GameView dialogs.
# ------------------------------------------------------

def remove_player_dialog():
    return messagebox.askquestion(
        "Remove Player",
        "Are you sure you want to remove this player? \
        \n\n(This doesn't actually do anything yet, so no one is removed.)\n"
    )

def quit_game_dialog():
    return messagebox.askquestion(
        "Quit Game",
        "Are you sure you want to quit this game?"
    )
