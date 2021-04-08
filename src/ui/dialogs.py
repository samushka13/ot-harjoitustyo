from tkinter import messagebox

# Login dialogs.

# Settings dialogs.

# Custom Questions dialogs.

def show_save_error_dialog():
    return messagebox.showinfo("Save Error", "Ensure that all fields have text in them.")

def show_save_successful_dialog():
    return messagebox.showinfo("Hooray!", "Question saved successfully. \n\n\
        Create more to improve the gaming experience.\n\n")

def show_delete_confirmation_dialog():
    return messagebox.askquestion("Delete", "Are you sure you want to delete the selected question?")

def show_delete_all_confirmation_dialog():
    return messagebox.askquestion("Delete", "Are you sure you want to delete all your questions?")

# Game session dialogs.
