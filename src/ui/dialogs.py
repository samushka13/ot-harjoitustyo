from tkinter import messagebox

# ------------------------------------------------------
# "What's new in this version?"
# ------------------------------------------------------

def whats_new_dialog():
    return messagebox.showinfo(
        "What's new",

"""These are currently working:

- Creating new credentials.
- Login with existing credentials.
- Login error handling from a UX perspective.
- LoginView.
- SettingsView (draft only, buttons lead nowhere).
- Testing the LoginServices class (83 %).

A few other things are working as well, but they weren't included in this release \
because a few things need to be resolved first.

The project's codebase includes a lot of work in progress due to prototyping, \
which is why parts of the repository and some of the code it contains are quite poorly made. \
This is not optimal, of course, but it was deemed necessary \
to quickly ensure the project is actually doable within the given time frame.

What to expect next week?

- CustomQuestionsView and its logic/services will be introduced.
- Settings-related tests will be formulated.
- Most of the code will be a whole lot 'cleaner' à la login-related code.

""",
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

def show_player_number_error():
    return messagebox.showinfo(
        "No players added",
        "At least one player must be added to start a new game.\
        \n\nYou can type in a custom name or select one from predefined values.\n"
    )

def show_player_name_error():
    return messagebox.showinfo(
        "Player name error",
        "Players must have unique names, but it seems that they are not."
    )

def show_category_number_error():
    return messagebox.showinfo(
        "Not enough categories",
        "At least two categories must be added to start a new game.\
        \n\nYou can select them using the category dropdown lists.\
        \n\nIf the lists are empty, try creating some questions in the Custom Questions view.\n"
    )

# ------------------------------------------------------
# CustomQuestionsView dialogs.
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
         \n\nCreate more to improve the gaming experience."
    )

def show_delete_confirmation_dialog(amount: int):
    if amount == 1:
        dialog = messagebox.askquestion(
            "Delete Item",
            "Are you sure you want to delete the selected question?"
        )
    else:
        dialog = messagebox.askquestion(
            "Delete Items",
            f"Are you sure you want to delete these {amount} selected questions?"
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
