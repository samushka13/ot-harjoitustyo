import tkinter as tk
from services.custom_content_services import custom_content_services
from ui.edit_view import EditView as edit_view
from ui.dialogs import (
    show_invalid_input_lengths,
    show_save_successful_dialog,
    show_delete_confirmation_dialog,
    show_delete_all_confirmation_dialog,
    show_delete_error_dialog,
    show_delete_all_information_dialog,
    show_edit_error_dialog,
)
from ui.stylings import (
    get_window_settings,
    CUSTOM_CONTENT_WINDOW_NAME,
    CUSTOM_CONTENT_WINDOW_SIZE,
    X, Y,
)
from ui.widgets import (
    title_label,
    basic_label,
    button,
    combobox,
    edit_textbox,
    listbox,
)


class CustomContentView:
    """Class that describes the UI of the custom questions view."""

    def __init__(self, service=custom_content_services):
        """Class constructor that initializes the class with appropriate services."""

        self.window = None
        self.service = service
        self.category_combobox = None
        self.difficulty_combobox = None
        self.question_entry = None
        self.answer_entry = None
        self.listbox =  None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, CUSTOM_CONTENT_WINDOW_NAME, CUSTOM_CONTENT_WINDOW_SIZE)
        self._build_layout()
        self._build_create_widgets()
        self._build_browse_widgets()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row configurations."""

        for i in (0,11):
            self.window.grid_rowconfigure(i, weight=3)

    def _build_create_widgets(self):
        """Builds the left-side widgets of the parent window."""

        title_label(self.window, "Create"
        ).grid(column=0, row=0, columnspan=2)

        basic_label(self.window, "Category"
        ).grid(column=0, row=1, columnspan=2)
        self.category_combobox = self._build_category_combobox()
        self.category_combobox.focus()

        basic_label(self.window, "Difficulty"
        ).grid(column=0, row=3, columnspan=2)
        self.difficulty_combobox = self._build_difficulty_combobox()

        basic_label(self.window, "Question"
        ).grid(column=0, row=5, columnspan=2)
        self.question_entry = edit_textbox(self.window, 6, 50)
        self.question_entry.grid(column=0, row=6, columnspan=2)

        basic_label(self.window, "Answer"
        ).grid(column=0, row=7, columnspan=2)
        self.answer_entry = edit_textbox(self.window, 4, 50)
        self.answer_entry.grid(column=0, row=8, columnspan=2)

        button(self.window, "Save", self._handle_save_event
        ).grid(column=0, row=9, pady=Y)
        button(self.window, "Clear", self._clear_entries
        ).grid(column=1, row=9, pady=Y)
        button(self.window, "Back to Settings", self._open_settings_view
        ).grid(column=0, row=11, columnspan=2, pady=Y)

    def _build_browse_widgets(self):
        """Builds the right-side widgets of the parent window."""

        title_label(self.window, "Browse"
        ).grid(column=2, row=0, columnspan=3)

        self.listbox = self._build_listbox()

        button(self.window, "Edit", self._handle_edit
        ).grid(column=2, row=11)
        button(self.window, "Delete selected", self._handle_delete_item
        ).grid(column=3, row=11)
        button(self.window, "Delete all", self._handle_delete_all
        ).grid(column=4, row=11)

    def _build_listbox(self):
        """Builds a listbox widget.

        Returns:
            A listbox with all question items in the database.
        """

        question_listbox = listbox()
        for entry in self.service.get_listbox_items():
            question_listbox.insert(tk.END, entry)
            question_listbox.select_set(0)
        question_listbox.grid(column=2, row=1, columnspan=3, rowspan=9, padx=X)

        return question_listbox

    def _build_category_combobox(self):
        """Builds a combobox widget.

        Returns:
            A combobox with all categories in the database.
        """

        category_combobox = combobox(self.window, 43)
        category_combobox['values'] = self.service.get_categories()
        category_combobox.grid(column=0, row=2, columnspan=2, padx=X)

        return category_combobox

    def _build_difficulty_combobox(self):
        """Builds a combobox widget.

        Returns:
            A combobox with the default difficulties.
        """

        difficulty_combobox = combobox(self.window, 43)
        difficulty_combobox['values'] = self.service.get_difficulties()
        difficulty_combobox.state(['readonly'])
        difficulty_combobox.set(self.service.get_difficulties()[1])
        difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)

        return difficulty_combobox

    def _handle_save_event(self):
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
            self.service.handle_save_item(category, difficulty, question, answer)
            show_save_successful_dialog()
            self._clear_entries()
            self._handle_widget_rebuild()

    def _clear_entries(self):
        """Clears all entry widgets to default values."""

        self.category_combobox.delete(0, 'end')
        self.category_combobox.set("")
        self.difficulty_combobox.set(self.service.get_difficulties()[1])
        self.question_entry.delete('1.0', 'end')
        self.answer_entry.delete('1.0', 'end')
        self.category_combobox.focus()

    def _handle_edit(self):
        """Calls CustomContentServices class methods to determine the question id and owner,
        then accommodates the UI accordingly."""

        selected = self.service.determine_question_ids(self.listbox)[0]
        if self.service.check_owner(selected) is True:
            self.window.destroy()
            edit_view(selected).initialize_window()
        else:
            show_edit_error_dialog()
            self.window.focus()

    def _handle_delete_item(self):
        """Shows a confirmation dialog, and, if the user confirms,
        calls CustomContentServices class methods which determine the question ids and
        handle item deletion, then accommodates the UI accordingly."""

        selected = self.service.determine_question_ids(self.listbox)
        if show_delete_confirmation_dialog(len(selected)) == "yes":
            deleted = self.service.delete_items(selected)
            if len(selected) > deleted:
                show_delete_error_dialog(len(selected)-deleted)
        self._handle_widget_rebuild()

    def _handle_delete_all(self):
        """Shows a confirmation dialog, and, if the user confirms,
        calls CustomContentServices class methods which handle item deletion.
        Then accommodates the UI accordingly."""

        if show_delete_all_confirmation_dialog() == "yes":
            deleted = self.service.delete_all()
            show_delete_all_information_dialog(deleted)
        self._handle_widget_rebuild()

    def _handle_widget_rebuild(self):
        """Rebuilds the widgets of the parent window and sets focus
        on the listbox widget."""

        self._build_create_widgets()
        self._build_browse_widgets()
        self.window.focus()
        self.listbox.focus()

    def _open_settings_view(self):
        """Destroys the current view and initialize a new one."""

        from ui.settings_view import settings_view
        self.window.destroy()
        settings_view.initialize_window()


custom_content_view = CustomContentView()
