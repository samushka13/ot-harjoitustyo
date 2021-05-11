import tkinter as tk
from tkinter import ttk, WORD, EXTENDED
from ui.stylings import BACKGROUND, TITLE_FONT, TEXT_FONT, BOARD_TEXT_FONT, BASIC_CURSOR

# ------------------------------------------------------
# Comboboxes.
# ------------------------------------------------------

def combobox(window=None, width=30):
    """Builds a tkinter combobox widget.

    Args:
        window (Tk): The parent window of the widget. Defaults to None.
        width (int): The width of the widget. Defaults to 30.

    Returns:
        default_combobox (Combobox): A combobox widget.
    """

    default_combobox = ttk.Combobox(
        window,
        width=width,
    )

    return default_combobox

# ------------------------------------------------------
# Labels.
# ------------------------------------------------------

def title_label(window=None, text=None):
    """Builds a tkinter label widget.

    Args:
        window (widget): The parent window of the widget. Defaults to None.
        text (str): The text shown on the label. Defaults to None.

    Returns:
        label (Label): A label widget for title text.
    """

    label = tk.Label(
        window,
        text=text,
        font=TITLE_FONT,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )

    return label

def basic_label(window=None, text=None):
    """Builds a tkinter label widget.

    Args:
        window (Tk): The parent window of the widget. Defaults to None.
        text (str): The text shown on the label. Defaults to None.

    Returns:
        label (Label): A label widget for basic text.
    """

    label = tk.Label(
        window,
        text=text,
        font=TEXT_FONT,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )

    return label

# ------------------------------------------------------
# Buttons.
# ------------------------------------------------------

def button(window=None, text=None, command=None):
    """Builds a tkinter button widget.
    The width of the button is determined dynamically based on the text length.

    Args:
        window (Tk): The parent window of the widget. Defaults to None.
        text (str): The text shown on the button. Defaults to None.
        command (method): Describes what the button does when pressed. Defaults to None.

    Returns:
        default_button (Button): A button widget.
    """

    if len(text) in range(0,10):
        width = 10
    elif len(text) in range(10,17):
        width = 15
    elif len(text) in range(17,25):
        width = 20
    elif len(text) in range(25,30):
        width = 25
    else:
        width = 30

    default_button = tk.Button(
        window,
        text=text,
        width=width,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
        command=command,
    )

    return default_button

# ------------------------------------------------------
# Entries.
# ------------------------------------------------------

def entry(window=None, width=30, show=None, textvariable=None):
    """Builds a tkinter entry widget.

    Args:
        window (Tk): The parent window of the widget. Defaults to None.
        width (int): The width of the widget. Defaults to 30.
        show (str): Masks the user input. Defaults to None.
        textvariable (StringVar): Required for getting the user input. Defaults to None.

    Returns:
        default_entry (Entry): An entry widget.
    """

    default_entry = tk.Entry(
        window,
        width=width,
        show=show,
        textvariable=textvariable,
    )

    return default_entry

# ------------------------------------------------------
# Textboxes.
# ------------------------------------------------------

def display_textbox(window, height, width, font=BOARD_TEXT_FONT):
    """Builds a tkinter textbox widget for display purposes only.

    Args:
        window (Tk): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.
        font (tuple): The font of the text. Defaults to BOARD_TEXT_FONT.

    Returns:
        textbox (Text): A disabled textbox widget.
    """

    textbox = tk.Text(
        window,
        height=height,
        width=width,
        font=font,
        cursor=BASIC_CURSOR,
        wrap=WORD,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )

    return textbox

def edit_textbox(window, height, width=50, font=TEXT_FONT):
    """Builds a tkinter textbox widget.

    Args:
        window (Tk): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget. Defaults to 50.
        font (tuple): The font of the text. Defaults to TEXT_FONT.

    Returns:
        textbox (Text): A textbox widget.
    """

    textbox = tk.Text(
        window,
        height=height,
        width=width,
        font=font,
        wrap=WORD,
        highlightbackground=BACKGROUND,
    )

    return textbox

# ------------------------------------------------------
# Listboxes.
# ------------------------------------------------------

def listbox(window=None, height=30, width=82):
    """Builds a tkinter listbox widget.

    Args:
        window (Tk): The parent window of the widget. Defaults to None.
        height (int): The height of the widget. Defaults to 30.
        width (int): The width of the widget. Defaults to 82.

    Returns:
        default_listbox (Listbox): A listbox widget.
    """

    default_listbox = tk.Listbox(
        window,
        height=height,
        width=width,
        highlightbackground=BACKGROUND,
        selectmode=EXTENDED,
    )

    return default_listbox

# ------------------------------------------------------
# Board elements.
# ------------------------------------------------------

def canvas(window, height, width):
    """Builds a tkinter canvas widget for drawing.

    Args:
        window (Tk): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.

    Returns:
        default_canvas (Canvas): A canvas widget.
    """

    default_canvas = tk.Canvas(
        window,
        height=height,
        width=width,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )

    return default_canvas

def board_segment(board, distance, extent, fill):
    """Builds a tkinter arc element on a canvas.

    Args:
        board (Canvas): The canvas on which the arc will be drawn.
        distance (float): Helps calculate the starting angle of the arc.
        extent (float): The length of the arc.
        fill (str): The color of the arc.

    Returns:
        segment (widget): A piece of the game board.
    """

    segment = board.create_arc(
        20, 20, 700, 700,
        start=360-distance,
        extent=-extent,
        fill=fill,
        width=3,
    )

    return segment
