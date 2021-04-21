from ui.bind_keys import bind_keys_to_widgets

# ------------------------------------------------------
# General window settings:
# ------------------------------------------------------

def get_window_settings(window, name, size):
    """Provides basic settings for windows of all views.

    Args:
        window (widget): The parent window of the widget.
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
RULES_WINDOW_SIZE = "740x660"
STATISTICS_WINDOW_SIZE = "720x720"

# ------------------------------------------------------
# Colors:
# ------------------------------------------------------

BACKGROUND = "white smoke"

# ------------------------------------------------------
# Fonts:
# ------------------------------------------------------

TITLE_FONT = ('Helvetica', 16, 'bold')
TEXT_FONT = ('Helvetica', 14)
TEXT_FONT_BOLD = ('Helvetica', 14, 'bold')
BOARD_TEXT_FONT = ('Helvetica', 18, 'bold')

# ------------------------------------------------------
# Paddings:
# ------------------------------------------------------

X = (30,30)
Y = (20,10)

# ------------------------------------------------------
# Cursors:
# ------------------------------------------------------

BASIC_CURSOR = "arrow"

# ------------------------------------------------------
# Die faces.
# Should be moved to Die class when such exists.
# ------------------------------------------------------

DIE_FACES = [
    (r'src/assets/die_1.png', 1),
    (r'src/assets/die_2.png', 2),
    (r'src/assets/die_3.png', 3),
    (r'src/assets/die_4.png', 4),
    (r'src/assets/die_5.png', 5),
    (r'src/assets/die_6.png', 6),
]
DEFAULT_DIE_FACE = r'src/assets/die_6.png'
