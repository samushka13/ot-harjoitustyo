import tkinter as tk
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
    get_combobox,
)
from ui.dialogs import (
    show_save_error_dialog,
    show_save_successful_dialog,
)

class EditView:
    """Class that describes the UI of the edit view.

    Attributes:
        database: The initialized database entity.
        service: The initialized service class entity.
        selected: The question class entity selected for editing.
    """

    def __init__(self, database, service, selected):
        """Class constructor that initializes the window
        with appropriate settings, database, services and widgets.

        Args:
            database: The initialized database entity.
            service: The initialized service class entity.
            selected: The question class entity selected for editing.
        """

        self.edit_window = tk.Tk()
        get_window_settings(self.edit_window, EDIT_QUESTION_WINDOW_NAME, EDIT_QUESTION_WINDOW_SIZE)
        self.database = database
        self.service = service
        self.selected = selected
        self._build_layout()
        self.question_entry = None
        self.answer_entry = None
        self.category_combobox = None
        self.difficulty_combobox = None
        self._build_widgets()
        self.edit_window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row configurations."""

        for i in (0,10):
            self.edit_window.grid_rowconfigure(i, weight=3)

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        get_title_label(self.edit_window, "Edit"
        ).grid(column=0, row=0, columnspan=2, padx=X)

        get_basic_label(self.edit_window, "Category"
        ).grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.category_combobox = get_combobox(self.edit_window, 43)
        self.category_combobox['values'] = self.database.get_categories()
        self.category_combobox.state(['readonly'])
        self.category_combobox.set(self.service.get_item_for_editing(self.selected)[0])
        self.category_combobox.grid(column=0, row=2, columnspan=2, padx=X)

        get_basic_label(self.edit_window, "Difficulty",
        ).grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        self.difficulty_combobox = get_combobox(self.edit_window, 43)
        self.difficulty_combobox['values'] = self.service.get_default_difficulties()
        self.difficulty_combobox.state(['readonly'])
        self.difficulty_combobox.set(self.service.get_item_for_editing(self.selected)[1])
        self.difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)

        get_basic_label(self.edit_window, "Question",
        ).grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        self.question_entry = get_edit_textbox(self.edit_window, 6, 50)
        self.question_entry.grid(column=0, row=6, columnspan=2, padx=X)
        self.question_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[2])

        get_basic_label(self.edit_window, "Answer",
        ).grid(column=0, row=7, columnspan=2, padx=X, pady=Y)

        self.answer_entry = get_edit_textbox(self.edit_window, 4, 50)
        self.answer_entry.grid(column=0, row=8, columnspan=2, padx=X)
        self.answer_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[3])

        get_basic_button(self.edit_window, "Save", self._handle_update
        ).grid(column=0, row=10)

        get_basic_button(self.edit_window, "Cancel", self.open_questions_view
        ).grid(column=1, row=10)

    def _handle_update(self):
        """Collects input values, calls CustomContentServices class methods
        which handle these values, and accommodates the UI accordingly."""

        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get("1.0",'end-1c')
        answer = self.answer_entry.get("1.0",'end-1c')
        if self.service.check_input_validity(category, difficulty, question, answer) is False:
            show_save_error_dialog()
            self.edit_window.focus()
            self.category_combobox.focus()
        else:
            self.service.update_item(self.selected, category, difficulty, question, answer)
            show_save_successful_dialog()
            self.open_questions_view()

    def open_questions_view(self):
        """Destroys the current view and initializes a new one."""

        from ui.custom_content_view import CustomContentView
        self.edit_window.destroy()
        CustomContentView(self.database)
