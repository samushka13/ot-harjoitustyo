from tkinter import messagebox


# -------------------------------------------------------------------------
# Login:
# -------------------------------------------------------------------------

def show_invalid_username_dialog():
    return messagebox.showinfo(
        "Invalid Username",
        "Username length should be 3-25 characters.",
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

def show_no_otdb_connection_dialog():
    return messagebox.showinfo(
            "Connection Error",
            "Could not connect to the Open Trivia Database.\
            \n\nThere are two possible reasons for this:\
            \n1. This device is not connected to the internet.\
            \n2. The Open Trivia Database servers are down.\
            \n\nIn any case, you can still play, but without any Open Trivia DB categories.\
            \n\nIf you don't have any other categories, now might be a good time to create some.\n",
        )

# -------------------------------------------------------------------------
# Settings:
# -------------------------------------------------------------------------

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

def show_about_otdb_dialog():
    return messagebox.showinfo(
            "About Open Trivia DB",
            """
Open Trivia Database is a free to use, user-contributed \
trivia question database available at https://opentdb.com/.

All questions provided by the Open Trivia DB API are available under the \
Creative Commons Attribution-ShareAlike 4.0 International License, \
and thus so are all such questions used in this program as well.
""",
        )

# -------------------------------------------------------------------------
# Custom Content:
# -------------------------------------------------------------------------

def show_invalid_input_lengths():
    return messagebox.showinfo(
        "Invalid input lengths",
        "Ensure that the text input lengths are within the following limits:\
        \n\nCategory: 1-30 characters\
        \nQuestion: 1-300 characters\
        \nAnswer: 1-100 characters\n"
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
        "A question can only be edited by the user who has created it.\
         \n\nYou can check the username at the end of the question.\n"
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
        f"{number} question was not deleted, as it belongs to another username."
    )
    else:
        dialog = messagebox.showinfo(
        "Delete Error",
        f"{number} questions were not deleted, as they belong to other usernames."
    )

    return dialog

def show_delete_all_confirmation_dialog():
    return messagebox.askquestion(
        "Delete All",
        "Are you sure you want to delete all your questions? \
        \n\nQuestions created by others will remain.\n"
    )

def show_delete_all_information_dialog(number: int):
    if number == 0:
        dialog = messagebox.showinfo(
        "Nothing to delete",
        "No questions were deleted, as they belong to other usernames."
    )
    else:
        dialog = messagebox.showinfo(
        "Delete Succesful",
        f"{number} questions were deleted."
    )

    return dialog

# -------------------------------------------------------------------------
# Game Sessions:
# -------------------------------------------------------------------------

def quit_game_dialog():
    return messagebox.askquestion(
        "Quit Game",
        "Are you sure you want to quit this game?"
    )

def show_player_victory_dialog(player: str):
    return messagebox.showinfo(
        "The game has ended",
        f"Congratulations, {player}, you are victorious!"
    )
