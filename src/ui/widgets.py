import tkinter as tk
from tkinter import ttk, WORD, EXTENDED
from ui.stylings import (
    BACKGROUND,
    TITLE_FONT,
    TEXT_FONT,
    BOARD_TEXT_FONT,
    BASIC_CURSOR,
)

# ------------------------------------------------------
# Comboboxes.
# ------------------------------------------------------

def get_combobox(window=None, width=30):
    """Builds a tkinter combobox widget.

    Args:
        window (widget): The parent window of the widget. Defaults to None.
        width (int, optional): The width of the widget. Defaults to 30.

    Returns:
        widget: A combobox.
    """
    combobox = ttk.Combobox(
        window,
        width=width,
    )
    return combobox

# ------------------------------------------------------
# Labels.
# ------------------------------------------------------

def get_title_label(window=None, text=None):
    """Builds a tkinter label widget.

    Args:
        window (widget): The parent window of the widget.
        text (str): The text shown on the label.

    Returns:
        widget: A label.
    """
    label = tk.Label(
        window,
        text=text,
        font=TITLE_FONT,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )
    return label

def get_basic_label(window=None, text=None):
    """Builds a tkinter label widget.

    Args:
        window (widget): The parent window of the widget.
        text (str): The text shown on the label.

    Returns:
        widget: A label.
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

def get_basic_button(window=None, text=None, command=None):
    """Builds a tkinter button widget.
    The width of the button is determined dynamically based on the text length.

    Args:
        window (widget): The parent window of the widget.
        text (str): The text shown on the button.
        command (command): Describes what the button does when pressed.

    Returns:
        widget: A button.
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
    button = tk.Button(
        window,
        text=text,
        width=width,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
        command=command,
    )
    return button

# ------------------------------------------------------
# Entries.
# ------------------------------------------------------

def get_basic_entry(window=None, width=30, show=None, textvariable=None):
    """Builds a tkinter entry widget.

    Args:
        window (widget): The parent window of the widget.
        width (int): The width of the widget.
        show (str, optional): Masks the user input. Defaults to None.
        textvariable (StringVar, optional): Required for getting the user input. Defaults to None.

    Returns:
        widget: An entry.
    """
    entry = tk.Entry(
        window,
        width=width,
        show=show,
        textvariable=textvariable,
    )
    return entry

# ------------------------------------------------------
# Textboxes.
# ------------------------------------------------------

def get_display_textbox(window, height, width, font=BOARD_TEXT_FONT):
    """Builds a tkinter textbox widget for display purposes only.

    Args:
        window (widget): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.
        font (font, optional): The font of the text. Defaults to BOARD_TEXT_FONT.

    Returns:
        widget: A disabled textbox.
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

def get_edit_textbox(window, height, width, font=TEXT_FONT):
    """Builds a tkinter textbox widget.

    Args:
        window (widget): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.
        font (font, optional): The font of the text. Defaults to TEXT_FONT.

    Returns:
        widget: A textbox.
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

def get_listbox(window=None, height=30, width=82):
    """Builds a tkinter listbox widget.

    Args:
        window (widget): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.

    Returns:
        widget: A listbox.
    """
    listbox = tk.Listbox(
        window,
        height=height,
        width=width,
        highlightbackground=BACKGROUND,
        selectmode=EXTENDED,
    )
    return listbox

# ------------------------------------------------------
# Board elements.
# ------------------------------------------------------

def get_canvas(window, height, width):
    """Builds a tkinter canvas widget for drawing.

    Args:
        window (widget): The parent window of the widget.
        height (int): The height of the widget.
        width (int): The width of the widget.

    Returns:
        widget: A canvas.
    """
    canvas = tk.Canvas(
        window,
        height=height,
        width=width,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )
    return canvas

def get_board_segment(canvas, distance: float, segment: float, fill):
    """Builds a tkinter arc element on a canvas.

    Args:
        canvas (widget): The canvas on which the arc will be drawn.
        distance (float): The starting angle of the arc.
        segment (float): The length of the arc.
        fill (color): The color of the arc.

    Returns:
        element: An arc.
    """
    segment = canvas.create_arc(
        20, 20, 700, 700,
        start=360-distance,
        extent=-segment,
        fill=fill,
        width=4,
    )
    return segment
