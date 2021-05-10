import tkinter as tk
from services.custom_content_services import custom_content_services
from ui.stylings import (
    get_window_settings,
    EDIT_QUESTION_WINDOW_NAME,
    EDIT_QUESTION_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    basic_label,
    title_label,
    button,
    edit_textbox,
    combobox,
)
from ui.dialogs import (
    show_invalid_input_lengths,
    show_save_successful_dialog,
)

class EditView:
    """Class that describes the UI of the edit view.

    Attributes:
        selected: The question class entity selected for editing.
        service: The current services class entity.
    """

    def __init__(self, selected, service=custom_content_services):
        """Class constructor that initializes the class with appropriate services.

        Args:
            selected: The question class entity selected for editing.
            service: The current services class entity.
        """

        self.window = None
        self.service = service
        self.selected = selected
        self.category_combobox = None
        self.difficulty_combobox = None
        self.question_entry = None
        self.answer_entry = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, EDIT_QUESTION_WINDOW_NAME, EDIT_QUESTION_WINDOW_SIZE)
        self._build_layout()
        self._build_widgets()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row configurations."""

        for i in (0,10):
            self.window.grid_rowconfigure(i, weight=3)

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        title_label(self.window, "Edit"
        ).grid(column=0, row=0, columnspan=2, padx=X)

        basic_label(self.window, "Category"
        ).grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.category_combobox = combobox(self.window, 43)
        self.category_combobox['values'] = self.service.get_categories()
        self.category_combobox.set(self.service.get_item_for_editing(self.selected)[0])
        self.category_combobox.grid(column=0, row=2, columnspan=2, padx=X)

        basic_label(self.window, "Difficulty",
        ).grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        self.difficulty_combobox = combobox(self.window, 43)
        self.difficulty_combobox['values'] = self.service.get_difficulties()
        self.difficulty_combobox.state(['readonly'])
        self.difficulty_combobox.set(self.service.get_item_for_editing(self.selected)[1])
        self.difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)

        basic_label(self.window, "Question",
        ).grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        self.question_entry = edit_textbox(self.window, 6, 50)
        self.question_entry.grid(column=0, row=6, columnspan=2, padx=X)
        self.question_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[2])

        basic_label(self.window, "Answer",
        ).grid(column=0, row=7, columnspan=2, padx=X, pady=Y)

        self.answer_entry = edit_textbox(self.window, 4, 50)
        self.answer_entry.grid(column=0, row=8, columnspan=2, padx=X)
        self.answer_entry.insert(tk.END, self.service.get_item_for_editing(self.selected)[3])

        button(self.window, "Save", self._handle_question_item_update
        ).grid(column=0, row=10)

        button(self.window, "Cancel", self._open_custom_content_view
        ).grid(column=1, row=10)

    def _handle_question_item_update(self):
        """Collects input values, calls CustomContentServices class methods
        which handle these values, and accommodates the UI accordingly."""

        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get("1.0",'end-1c')
        answer = self.answer_entry.get("1.0",'end-1c')
        if self.service.check_input_length_validity(category, question, answer) is False:
            show_invalid_input_lengths()
            self.window.focus()
            self.category_combobox.focus()
        else:
            self.service.update_item(self.selected, category, difficulty, question, answer)
            show_save_successful_dialog()
            self._open_custom_content_view()

    def _open_custom_content_view(self):
        """Destroys the current view and initializes a new one."""

        from ui.custom_content_view import custom_content_view
        self.window.destroy()
        custom_content_view.initialize_window()
