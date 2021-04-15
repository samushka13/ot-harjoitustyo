from services.bind_keys import bind_keys_to_widgets
from ui.stylings import BACKGROUND

def get_window_settings(window, name, size):
    """Provides basic settings for windows of all views.

    Args:
        window: Value of the tkinter window widget.
        name: String value of the window title.
        size: String value of the window size.
    """

    window.title(name)
    window.geometry(size)
    window.resizable(False, False)
    window.configure(bg=BACKGROUND)
    bind_keys_to_widgets(window)
    window.focus()
