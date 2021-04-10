from tkinter import messagebox
from services.database_operations import get_sorted_users

# Login dialogs.

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

def show_users_dialog():
    if len(get_sorted_users()) > 0:
        dialog = messagebox.showinfo(
            "Users",
            f"List of users on this device: \n\n{get_sorted_users()}",
        )
    else:
        dialog = messagebox.showinfo(
            "Users",
            "There are currently no users on this device.",
        )
    return dialog

# Settings dialogs.

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

# Custom Questions dialogs.

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

# Game session dialogs.

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
