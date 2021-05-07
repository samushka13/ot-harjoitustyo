import platform
from ui.bind_keys import bind_keys_to_widgets

# ------------------------------------------------------
# General window settings:
# ------------------------------------------------------

def get_window_settings(window, name, size):
    """Provides basic settings for windows of all views.

    Args:
        window (Tk): The parent window of the widget.
        name (str): The name of the window.
        size (str): The size of the window.
    """

    window.title(name)
    window.geometry(size)
    window.resizable(False, False)
    window.configure(bg=BACKGROUND)
    bind_keys_to_widgets(window)
    window.focus()

# ------------------------------------------------------
# Window names:
# ------------------------------------------------------

LOGIN_WINDOW_NAME = "Trivioboros"
SETTINGS_WINDOW_NAME = "Trivioboros"
CUSTOM_CONTENT_WINDOW_NAME = "Trivioboros"
EDIT_QUESTION_WINDOW_NAME = "Trivioboros"
BOARD_WINDOW_NAME = "Trivioboros"
RULES_WINDOW_NAME = "Rules of the Game"
STATISTICS_WINDOW_NAME = "Statistics"

# ------------------------------------------------------
# Window sizes:
# ------------------------------------------------------

LOGIN_WINDOW_SIZE = "360x360"
SETTINGS_WINDOW_SIZE = "920x720"
CUSTOM_CONTENT_WINDOW_SIZE = "1280x720"
EDIT_QUESTION_WINDOW_SIZE = "480x600"
BOARD_WINDOW_SIZE = "1280x720"
RULES_WINDOW_SIZE = "730x620"
STATISTICS_WINDOW_SIZE = "360x300"

# ------------------------------------------------------
# Colors:
# ------------------------------------------------------

BACKGROUND = "white smoke"

# ------------------------------------------------------
# Fonts:
# ------------------------------------------------------

if platform.system() == 'Darwin':
    TITLE_FONT = ('Helvetica', 16, 'bold')
    TEXT_FONT = ('Helvetica', 14)
    BOARD_TEXT_FONT = ('Helvetica', 18, 'bold')
if platform.system() == 'Windows':
    TITLE_FONT = ('Segoe UI', 16, 'bold')
    TEXT_FONT = ('Segoe UI', 14)
    BOARD_TEXT_FONT = ('Segoe UI', 18, 'bold')
if platform.system() == 'Linux':
    TITLE_FONT = ('Ubuntu Monospace', 16, 'bold')
    TEXT_FONT = ('Ubuntu Monospace', 14)
    BOARD_TEXT_FONT = ('Ubuntu Monospace', 18, 'bold')

# ------------------------------------------------------
# Paddings:
# ------------------------------------------------------

X = (30,30)
Y = (20,10)

# ------------------------------------------------------
# Cursors:
# ------------------------------------------------------

BASIC_CURSOR = "arrow"
