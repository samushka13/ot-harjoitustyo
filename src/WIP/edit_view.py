import tkinter as tk
from tkinter import ttk
from ui.stylings import (
    get_window_settings,
    EDIT_QUESTION_WINDOW_NAME,
    EDIT_QUESTION_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    get_basic_label,
    get_title_label,
    get_basic_button,
    get_edit_textbox,
)
from ui.dialogs import (
    show_save_error_dialog,
    show_save_successful_dialog,
)

class EditView:
    def __init__(self, database, service, selected):
        self.edit_window = tk.Tk()
        get_window_settings(self.edit_window, EDIT_QUESTION_WINDOW_NAME, EDIT_QUESTION_WINDOW_SIZE)

        self.database = database
        self.service = service

        self.selected = selected

        for i in (0,10):
            self.edit_window.grid_rowconfigure(i, weight=3)

        get_title_label(
            self.edit_window,
            "Edit",
        ).grid(column=0, row=0, columnspan=2, padx=X)

        get_basic_label(
            self.edit_window,
            "Category",
        ).grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.category_combobox = ttk.Combobox(self.edit_window, width=43)
        self.category_combobox['values'] = self.database.get_categories()
        self.category_combobox.state(['readonly'])
        self.category_combobox.set(self.service.get_item_for_editing(self.selected)[0])
        self.category_combobox.grid(column=0, row=2, columnspan=2, padx=X)

        get_basic_label(
            self.edit_window,
            "Difficulty",
        ).grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        self.difficulty_combobox = ttk.Combobox(self.edit_window, width=43)
        self.difficulty_combobox['values'] = self.service.get_default_difficulties()
        self.difficulty_combobox.state(['readonly'])
        self.difficulty_combobox.set(self.service.get_item_for_editing(self.selected)[1])
        self.difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)

        get_basic_label(
            self.edit_window,
            "Question",
        ).grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        self.question_entry = get_edit_textbox(
            self.edit_window,
            height=6,
            width=50,
        )
        self.question_entry.grid(column=0, row=6, columnspan=2, padx=X)
        self.question_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[2])

        get_basic_label(
            self.edit_window,
            "Answer",
        ).grid(column=0, row=7, columnspan=2, padx=X, pady=Y)

        self.answer_entry = get_edit_textbox(
            self.edit_window,
            height=4,
            width=50,
        )
        self.answer_entry.grid(column=0, row=8, columnspan=2, padx=X)
        self.answer_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[3])

        get_basic_button(
            self.edit_window,
            "Save",
            command=self._update_item,
        ).grid(column=0, row=10)

        get_basic_button(
            self.edit_window,
            "Cancel",
            command=self.open_questions_view,
        ).grid(column=1, row=10)

        self.edit_window.mainloop()

    def _update_item(self):
        question_id = self.selected
        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get("1.0",'end-1c')
        answer = self.answer_entry.get("1.0",'end-1c')
        if "" in (category, difficulty, question, answer):
            show_save_error_dialog()
            self.edit_window.focus()
            self.category_combobox.focus()
        else:
            if question.endswith('?') is False:
                question = question + "?"
            if answer.endswith('.') is False:
                if answer.endswith('!') is False:
                    answer = answer + "."
            self.service.update_item(question_id, category, difficulty, question, answer)
            show_save_successful_dialog()
            self.open_questions_view()

    def open_questions_view(self):
        from ui.custom_content_view import CustomContentView
        self.edit_window.destroy()
        CustomContentView(self.database)
