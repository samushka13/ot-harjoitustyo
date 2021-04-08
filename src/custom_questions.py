import tkinter as tk
from tkinter import ttk
from ui.stylings import (
    CUSTOM_QUESTIONS_WINDOW_NAME,
    CUSTOM_QUESTIONS_WINDOW_SIZE,
    BACKGROUND,
    X,
    Y,
    TITLE_FONT,
)
from ui.dialogs import (
    show_save_error_dialog,
    show_save_successful_dialog,
    show_delete_confirmation_dialog,
    show_delete_all_confirmation_dialog,
)
from services.database_connection import db
from services.database_operations import (
    save_item_to_database,
    delete_item_from_database,
    delete_all_users_items_from_database,
)
from entities.settings import DIFFICULTY_NAMES

class CustomQuestionsView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(CUSTOM_QUESTIONS_WINDOW_NAME)
        self.window.geometry(CUSTOM_QUESTIONS_WINDOW_SIZE)
        self.window.resizable(False, False)
        self.window.configure(bg=BACKGROUND)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)
        self.window.focus()

        self.window.grid_rowconfigure(0, weight=2)
        self.window.grid_rowconfigure(11, weight=2)

        # -------------------------------------------------------------------
        # Left-side widgets start.
        # -------------------------------------------------------------------

        title = tk.Label(self.window, text="Create", font=TITLE_FONT)
        title.grid(column=0, row=0, columnspan=2, padx=X, pady=Y)

        label = tk.Label(self.window, text="Category")
        label.grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.get_category_combobox()
        self.category_combobox.focus()

        label = tk.Label(self.window, text="Difficulty")
        label.grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        self.get_difficulty_combobox()

        label = tk.Label(self.window, text="Question")
        label.grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        self.question_entry = tk.Entry(self.window, width=50)
        self.question_entry.grid(column=0, row=6, columnspan=2, padx=X, pady=Y)

        label = tk.Label(self.window, text="Answer")
        label.grid(column=0, row=7, columnspan=2, padx=X, pady=Y)

        self.answer_entry = tk.Entry(self.window, width=50)
        self.answer_entry.grid(column=0, row=8, columnspan=2, padx=X, pady=Y)

        save = tk.Button(self.window, text="Save", width=10, command=self.save_item)
        save.grid(column=0, row=9, padx=X, pady=Y)

        clear = tk.Button(self.window, text="Clear", width=10, command=self.clear_item)
        clear.grid(column=1, row=9, padx=X, pady=Y)

        clear = tk.Button(self.window, text="Back to Settings", width=20, command=self.open_settings_view)
        clear.grid(column=0, row=11, columnspan=2, padx=X, pady=Y)

        # -------------------------------------------------------------------
        # Left-side widgets end.
        # -------------------------------------------------------------------
        # Right-side widgets start.
        # -------------------------------------------------------------------

        title = tk.Label(self.window, text="Browse", font=TITLE_FONT)
        title.grid(column=2, row=0, columnspan=3, padx=X, pady=Y)

        self.get_listbox()

        edit = tk.Button(self.window, text="Edit", width=10, command=self.edit_item)
        edit.grid(column=2, row=11, padx=X, pady=Y)

        delete = tk.Button(self.window, text="Delete", width=10, command=self.delete_item)
        delete.grid(column=3, row=11, padx=X, pady=Y)

        delete_all = tk.Button(self.window, text="Delete all", width=10, command=self.delete_all)
        delete_all.grid(column=4, row=11, padx=X, pady=Y)

        # -------------------------------------------------------------------
        # Right-side widgets end.
        # -------------------------------------------------------------------

        self.window.mainloop()

    def save_item(self):
        user_id = 1
        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if "" in (category, difficulty, question, answer):
            show_save_error_dialog()
            self.window.focus()
            self.category_combobox.focus()
        else:
            if question.endswith('?') is False:
                question = question + "?"
            if answer.endswith('.') is False:
                answer = answer + "."
            save_item_to_database(user_id, category, difficulty, question, answer)
            show_save_successful_dialog()
            self.clear_item()
            self.get_listbox()
            self.get_category_combobox()
            self.window.focus()
            self.category_combobox.focus()

    def clear_item(self):
        self.category_combobox.delete(0, 'end')
        self.difficulty_combobox.delete(0, 'end')
        self.question_entry.delete(0, 'end')
        self.answer_entry.delete(0, 'end')
        self.category_combobox.focus()

    def edit_item(self):

        # UPDATE Questions SET ... = ... WHERE ... = ...

        pass

    def delete_item(self):
        confirmation = show_delete_confirmation_dialog()
        if confirmation == 'yes':
            delete_item_from_database(str(self.listbox.get(self.listbox.curselection())).split(' ', 1)[0])
            self.get_listbox()
            self.get_category_combobox()
            self.window.focus()
            self.listbox.focus()

    def delete_all(self):
        confirmation = show_delete_all_confirmation_dialog()
        if confirmation == 'yes':
            delete_all_users_items_from_database()
            self.get_listbox()
            self.get_category_combobox()
            self.window.focus()
            self.listbox.focus()

        # These will be used to enable a feature,
        # where the current user can view every user's questions (in the same database),
        # but only delete (or edit) their own.
        # user_id = db.execute(f"SELECT id FROM Users WHERE username='{current_user}'").fetchone()
        # db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")

    def get_listbox(self):
        entries = []
        for row in db.execute("SELECT id, category, difficulty, question, answer FROM Questions").fetchall():
            entries.append(f"{row['id']}. | {row['category']} | {row['difficulty']} | {row['question']} | {row['answer']}")
        self.listbox_entries = entries
        self.listbox = tk.Listbox(self.window, width=80, height=32)
        for entry in self.listbox_entries:
            self.listbox.insert(tk.END, entry)
            self.listbox.select_set(0)
        self.listbox.grid(column=2, row=1, columnspan=3, rowspan=9, padx=X, pady=Y)
        return self.listbox

    def get_category_combobox(self):
        self.category_combobox = ttk.Combobox(self.window, width=50, textvariable=tk.StringVar())
        values = []
        for row in db.execute("SELECT category FROM Questions GROUP BY category").fetchall():
            values.append(f"{row['category']}")
        self.category_combobox['values'] = values
        self.category_combobox.grid(column=0, row=2, columnspan=2, padx=X, pady=Y)
        return self.category_combobox

    def get_difficulty_combobox(self):
        self.difficulty_combobox = ttk.Combobox(self.window, width=50, textvariable=tk.StringVar())
        self.difficulty_combobox['values'] = DIFFICULTY_NAMES
        self.difficulty_combobox.state(['readonly'])
        self.difficulty_combobox.set(DIFFICULTY_NAMES[1])
        self.difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X, pady=Y)
        return self.difficulty_combobox

    def bind_key_to_button(self, window):
        window.widget.invoke()

    def open_settings_view(self):
        from settings import SettingsView
        self.window.destroy()
        SettingsView()
