import tkinter as tk
from services.custom_content_services import CustomContentServices
from ui.dialogs import (
    show_save_error_dialog,
    show_save_successful_dialog,
    show_delete_confirmation_dialog,
    show_delete_all_confirmation_dialog,
    show_delete_error_dialog,
    show_edit_error_dialog,
    show_edit_not_ready_dialog,
)
from ui.stylings import (
    get_window_settings,
    CUSTOM_CONTENT_WINDOW_NAME,
    CUSTOM_CONTENT_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    get_title_label,
    get_basic_label,
    get_basic_button,
    get_combobox,
    get_edit_textbox,
    get_listbox,
)

class CustomContentView:
    """Class that describes the UI of the custom questions view.

    Attributes:
        database: Value of the initialized database.
        Only passed on to CustomContentServices class.
        This is not optimal, but will be changed when
        a new way of starting the app is implemented.
    """

    def __init__(self, database):
        """Class constructor that initializes the window
        with appropriate settings, services and widgets.

        Args:
            database: Value of the initialized database.
        """

        self.window = tk.Tk()
        get_window_settings(self.window, CUSTOM_CONTENT_WINDOW_NAME, CUSTOM_CONTENT_WINDOW_SIZE)
        self.database = database
        self.service = CustomContentServices(self.window, self.database)
        self._build_layout()
        self.question_entry = None
        self.answer_entry = None
        self.category_combobox = None
        self.difficulty_combobox = None
        self.listbox =  None
        self._build_widgets()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row configurations."""

        for i in (0,11):
            self.window.grid_rowconfigure(i, weight=3)

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        # -------------------------------------------------------------------
        # Left-side widgets:
        # -------------------------------------------------------------------

        get_title_label(self.window, "Create").grid(column=0, row=0, columnspan=2)

        get_basic_label(self.window, "Category").grid(column=0, row=1, columnspan=2)
        self.category_combobox = self._build_category_combobox()
        self.category_combobox.focus()

        get_basic_label(self.window, "Difficulty").grid(column=0, row=3, columnspan=2)
        self.difficulty_combobox = self._build_difficulty_combobox()

        get_basic_label(self.window, "Question").grid(column=0, row=5, columnspan=2)
        self.question_entry = get_edit_textbox(self.window, 6, 50)
        self.question_entry.grid(column=0, row=6, columnspan=2)

        get_basic_label(self.window, "Answer").grid(column=0, row=7, columnspan=2)
        self.answer_entry = get_edit_textbox(self.window, 4, 50)
        self.answer_entry.grid(column=0, row=8, columnspan=2)

        get_basic_button(self.window, "Save", self._handle_save).grid(column=0, row=9, pady=Y)
        get_basic_button(self.window, "Clear", self._clear_entries).grid(column=1, row=9, pady=Y)
        get_basic_button(self.window, "Back to Settings", self._open_settings_view
        ).grid(column=0, row=11, columnspan=2, pady=Y)

        # -------------------------------------------------------------------
        # Right-side widgets:
        # -------------------------------------------------------------------

        get_title_label(self.window, "Browse"
        ).grid(column=2, row=0, columnspan=3)
        self.listbox = self._build_listbox()
        get_basic_button(self.window, "Edit", self._handle_edit).grid(column=2, row=11)
        get_basic_button(self.window, "Delete Selected", self._handle_delete_item
        ).grid(column=3, row=11)
        get_basic_button(self.window, "Delete all", self._handle_delete_all).grid(column=4, row=11)

    def _build_listbox(self):
        """Builds a listbox widget.

        Returns:
            A listbox with all question items in the database.
        """

        listbox = get_listbox(self.window, 30, 82)
        for entry in self.service.get_listbox_items():
            listbox.insert(tk.END, entry)
            listbox.select_set(0)
        listbox.grid(column=2, row=1, columnspan=3, rowspan=9, padx=X)
        return listbox

    def _build_category_combobox(self):
        """Builds a combobox widget.

        Returns:
            A combobox with all categories in the database.
        """

        category_combobox = get_combobox(self.window, 43)
        category_combobox['values'] = self.service.get_categories()
        category_combobox.grid(column=0, row=2, columnspan=2, padx=X)
        return category_combobox

    def _build_difficulty_combobox(self):
        """Builds a combobox widget.

        Returns:
            A combobox with the default difficulties.
        """

        difficulty_combobox = get_combobox(self.window, 43)
        difficulty_combobox['values'] = self.service.get_difficulties()
        difficulty_combobox.state(['readonly'])
        difficulty_combobox.set(self.service.get_difficulties()[1])
        difficulty_combobox.grid(column=0, row=4, columnspan=2, padx=X)
        return difficulty_combobox

    # -------------------------------------------------------------------
    # These methods handle button commands:
    # -------------------------------------------------------------------

    def _handle_save(self):
        """Collects input values, calls CustomContentServices class methods
        which handle these values, and accommodates the UI accordingly."""

        category = self.category_combobox.get()
        difficulty = self.difficulty_combobox.get()
        question = self.question_entry.get("1.0",'end-1c')
        answer = self.answer_entry.get("1.0",'end-1c')
        if self.service.check_input_validity(category, difficulty, question, answer) is False:
            show_save_error_dialog()
            self.window.focus()
            self.category_combobox.focus()
        else:
            self.service.handle_save_item(category, difficulty, question, answer)
            show_save_successful_dialog()
            self._clear_entries()
            self._build_widgets()
            self.window.focus()
            self.category_combobox.focus()

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

        show_edit_not_ready_dialog()

        # from ui.edit_view import EditView

        # selected = self.service.determine_question_ids(self.listbox)[0]
        # if self.service.check_owner(selected) is True:
        #     self.window.destroy()
        #     EditView(self.database, self.service, selected)
        # else:
        #     show_edit_error_dialog()
        #     self.window.focus()

    def _handle_delete_item(self):
        """Shows a confirmation dialog, and, if the user confirms,
        calls CustomContentServices class methods which determine the question ids and
        handle item deletion, then accommodates the UI accordingly."""

        selected = self.service.determine_question_ids(self.listbox)
        if show_delete_confirmation_dialog(len(selected)) == "yes":
            deleted = self.service.delete_items(selected)
            if len(selected) > (deleted):
                show_delete_error_dialog(len(selected)-(deleted))
            self._build_widgets()
            self.window.focus()
            self.listbox.focus()

    def _handle_delete_all(self):
        """Shows a confirmation dialog, and, if the user confirms,
        calls CustomContentServices class methods which handle item deletion.
        Then accommodates the UI accordingly."""

        if show_delete_all_confirmation_dialog() == "yes":
            self.service.delete_all()
            self._build_widgets()
            self.window.focus()
            self.listbox.focus()

    def _open_settings_view(self):
        """Destroys the current view and initialize a new one."""

        from ui.settings_view import SettingsView
        self.window.destroy()
        SettingsView(self.database)
