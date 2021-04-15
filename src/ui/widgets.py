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

def get_combobox(window, width=30):
    combobox = ttk.Combobox(
        window,
        width=width,
    )
    return combobox

# ------------------------------------------------------
# Labels.
# ------------------------------------------------------

def get_title_label(window, text: str):
    label = tk.Label(
        window,
        text=text,
        font=TITLE_FONT,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )
    return label

def get_basic_label(window, text: str):
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

def get_basic_button(window, text: str, command):
    if len(text) in range(0,10):
        width = 10
    elif len(text) in range(10,17):
        width = 15
    elif len(text) in range(17,23):
        width = 20
    elif len(text) in range(23,28):
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

def get_basic_entry(window, width: int, show=None, textvariable=None):
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

def get_display_textbox(window, height: int, width: int, font=BOARD_TEXT_FONT):
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

def get_edit_textbox(window, height: int, width: int, font=TEXT_FONT):
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

def get_listbox(window, height: int, width: int):
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

def get_canvas(window, height: int, width: int):
    canvas = tk.Canvas(
        window,
        height=height,
        width=width,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )
    return canvas

def get_board_segment(canvas, distance: float, segment: float, fill):
    segment = canvas.create_arc(
        20, 20, 700, 700,
        start=360-distance,
        extent=-segment,
        fill=fill,
        width=4,
    )
    return segment
