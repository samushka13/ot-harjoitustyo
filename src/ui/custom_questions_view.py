import tkinter as tk
from tkinter import ttk, WORD, EXTENDED, ACTIVE
from services.custom_questions_services import CustomQuestionsServices
from services.ui_services import get_window_settings
from ui.edit_view import EditView
from ui.dialogs import (
    show_save_error_dialog,
    show_save_successful_dialog,
    show_delete_confirmation_dialog,
    show_delete_all_confirmation_dialog,
)
from ui.stylings import (
    CUSTOM_QUESTIONS_WINDOW_NAME,
    CUSTOM_QUESTIONS_WINDOW_SIZE,
    BACKGROUND,
    X,
    Y,
    TITLE_FONT,
    TEXT_FONT,
)

class CustomQuestionsView:
    def __init__(self, database):
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            CUSTOM_QUESTIONS_WINDOW_NAME,
            CUSTOM_QUESTIONS_WINDOW_SIZE,
        )

        self.service = CustomQuestionsServices(self.window, database)
        self.database = database

        for i in (0,11):
            self.window.grid_rowconfigure(i, weight=3)

        # -------------------------------------------------------------------
        # Left-side widgets start here.
        # -------------------------------------------------------------------

        title = tk.Label(
            self.window,
            text="Create",
            font=TITLE_FONT,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        title.grid(column=0, row=0, columnspan=2)

        label = tk.Label(
            self.window,
            text="Category",
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        label.grid(column=0, row=1, columnspan=2)

        self.build_category_combobox()
        self.category_combobox.focus()

        label = tk.Label(
            self.window,
            text="Difficulty",
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        label.grid(column=0, row=3, columnspan=2)

        self.build_difficulty_combobox()

        label = tk.Label(
            self.window,
            text="Question",
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        label.grid(column=0, row=5, columnspan=2)

        self.question_entry = tk.Text(
            self.window,
            height=6,
            width=50,
            font=TEXT_FONT,
            wrap=WORD,
            highlightbackground=BACKGROUND,
        )
        self.question_entry.grid(column=0, row=6, columnspan=2)

        label = tk.Label(
            self.window,
            text="Answer",
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        label.grid(column=0, row=7, columnspan=2)

        self.answer_entry = tk.Text(
            self.window,
            height=4,
            width=50,
            font=TEXT_FONT,
            wrap=WORD,
            highlightbackground=BACKGROUND,
        )
        self.answer_entry.grid(column=0, row=8, columnspan=2)

        save = tk.Button(
            self.window,
            text="Save",
            width=10,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.save_item,
        )
        save.grid(column=0, row=9, pady=Y)

        clear = tk.Button(
            self.window,
            text="Clear",
            width=10,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.clear_item,
        )
        clear.grid(column=1, row=9, pady=Y)

        clear = tk.Button(
            self.window,
            text="Back to Settings",
            width=20,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.open_settings_view,
        )
        clear.grid(column=0, row=11, columnspan=2)

        # -------------------------------------------------------------------
        # Left-side widgets end here.
        # -------------------------------------------------------------------
        # Right-side widgets start here.
        # -------------------------------------------------------------------

        title = tk.Label(
            self.window,
            text="Browse",
            font=TITLE_FONT,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
        )
        title.grid(column=2, row=0, columnspan=3)

        self.build_listbox()

        edit = tk.Button(
            self.window,
            text="Edit",
            width=10,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.edit_item,
        )
        edit.grid(column=2, row=11)

        delete = tk.Button(
            self.window,
            text="Delete Selected",
            width=15,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.delete_items,
        )
        delete.grid(column=3, row=11)

        delete_all = tk.Button(
            self.window,
            text="Delete all",
            width=10,
            bg=BACKGROUND,
            highlightbackground=BACKGROUND,
            command=self.delete_all,
        )
        delete_all.grid(column=4, row=11)

        # -------------------------------------------------------------------
        # Right-side widgets end here.
        # -------------------------------------------------------------------

        self.window.mainloop()

    # -------------------------------------------------------------------
    # These functions build widgets:
    # -------------------------------------------------------------------

    def build_listbox(self):
        self.listbox = tk.Listbox(
            self.window,
            width=82,
            height=30,
            highlightbackground=BACKGROUND,
            selectmode=EXTENDED,
        )
        for entry in self.database.get_listbox_items():
            self.listbox.insert(tk.END, entry)
            self.listbox.select_set(0)
        self.listbox.grid(column=2, row=1, columnspan=3, rowspan=9, padx=X)
        return self.listbox

    def build_category_combobox(self):
        self.category_combobox = ttk.Combobox(self.window, width=43)
        self.category_combobox['values'] = self.database.get_categories()
        self.category_combobox.grid(column=0, row=2, columnspan=2, padx=X)
        return self.category_combobox

    def build_difficulty_combobox(self):
        from services.settings_services import SettingsServices
        values = SettingsServices(self.window, self.database).get_default_difficulties()
        self.difficulty_combobox = ttk.Combobox(self.window, width=43)
        self.difficulty_combobox['values'] = values
        self.difficulty_combobox.state(['readonly'])
        self.difficulty_combobox.set(values[1])
        self.difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)
        return self.difficulty_combobox

    # -------------------------------------------------------------------
    # These functions process button commands:
    # -------------------------------------------------------------------

    def save_item(self):
        # This needs to be modified to actually work with real user_id numbers.
        user_id = 1
        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get("1.0",'end-1c')
        answer = self.answer_entry.get("1.0",'end-1c')
        if "" in (category, difficulty, question, answer):
            show_save_error_dialog()
            self.window.focus()
            self.category_combobox.focus()
        else:
            if question.endswith('?') is False:
                question = question + "?"
            if answer.endswith('.') is False:
                if answer.endswith('!') is False:
                    answer = answer + "."
            self.database.save_item_to_database(user_id, category, difficulty, question, answer)
            show_save_successful_dialog()
            self.clear_item()
            self.build_listbox()
            self.build_category_combobox()
            self.window.focus()
            self.category_combobox.focus()

    def clear_item(self):
        self.category_combobox.delete(0, 'end')
        self.difficulty_combobox.delete(0, 'end')
        self.question_entry.delete('1.0', 'end')
        self.answer_entry.delete('1.0', 'end')
        self.category_combobox.focus()

    def edit_item(self):
        selected = self.listbox.get(ACTIVE).split(' ', 1)[0]
        self.window.destroy()
        EditView(self.database, self.service, selected)

    def delete_items(self):
        selected = [self.listbox.get(i).split(' ', 1)[0] for i in self.listbox.curselection()]
        if show_delete_confirmation_dialog(len(selected)) == "yes":
            for item in selected:
                self.database.delete_item_from_database(item)
            self.build_listbox()
            self.build_category_combobox()
            self.window.focus()
            self.listbox.focus()

    def delete_all(self):
        if show_delete_all_confirmation_dialog() == "yes":
            self.database.delete_all_user_items_from_database()
            self.build_listbox()
            self.build_category_combobox()
            self.window.focus()
            self.listbox.focus()

    def open_settings_view(self):
        from ui.settings_view import SettingsView
        self.window.destroy()
        SettingsView(self.database)