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

# Settings dialogs. (Currently none.)

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
        \n\nQuestions created by others will remain."
    )

# Game session dialogs.

def remove_player_dialog():
    return messagebox.askquestion(
        "Remove Player",
        "Are you sure you want to remove this player? \
        \n\n(This doesn't actually do anything yet, so no one is removed.)"
    )

def quit_game_dialog():
    return messagebox.askquestion(
        "Quit Game",
        "Are you sure you want to quit this game?"
    )
