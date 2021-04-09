from services.bind_keys import bind_keys_to_widgets
from ui.stylings import BACKGROUND

def get_window_settings(window, name, size):
    window.title(name)
    window.geometry(size)
    window.resizable(False, False)
    window.configure(bg=BACKGROUND)
    bind_keys_to_widgets(window)
    window.focus()
