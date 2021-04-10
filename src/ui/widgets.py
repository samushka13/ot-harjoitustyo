import tkinter as tk
from tkinter import ttk, WORD
from services.database_operations import get_categories
from entities.settings import (
    NUMBER_OF_PLAYERS,
    BOARD_SIZE_NAMES,
    SEGMENT,
)
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

def get_players_combobox(window):
    players_combobox = ttk.Combobox(window, width=30)
    values = players_combobox['values'] = NUMBER_OF_PLAYERS
    players_combobox.state(['readonly'])
    players_combobox.set(values[0])
    players_combobox.grid(column=0, row=2, columnspan=2)
    return players_combobox, players_combobox.focus()

def get_board_size_combobox(window):
    board_size_combobox = ttk.Combobox(window, width=30)
    board_size_combobox['values'] = BOARD_SIZE_NAMES
    board_size_combobox.state(['readonly'])
    board_size_combobox.set(BOARD_SIZE_NAMES[2])
    board_size_combobox.grid(column=0, row=4, columnspan=2)
    return board_size_combobox

def get_category_comboboxes(window):
    comboboxes = []
    i = 0
    for i in range(0,5):
        category_combobox = ttk.Combobox(window, width=30)
        categories = get_categories()
        category_combobox['values'] = categories
        category_combobox.state(['readonly'])
        if len(categories) < 5:
            if len(categories) == 0:
                category_combobox.set("")
            else:
                category_combobox.set(categories[0])
        else:
            category_combobox.set(categories[i])
        category_combobox.grid(column=0, row=6+i, columnspan=2)
        comboboxes.append(category_combobox)
        i += 1
    return comboboxes

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

def get_basic_label(window, text: str, font=TEXT_FONT):
    label = tk.Label(
        window,
        text=text,
        font=font,
        bg=BACKGROUND,
        highlightbackground=BACKGROUND,
    )
    return label

# ------------------------------------------------------
# Buttons.
# ------------------------------------------------------

def get_basic_button(window, text: str, width: int, command):
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

def get_basic_entry(window, width: int, show=None):
    entry = tk.Entry(
        window,
        width=width,
        show=show,
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

def get_board_segment(canvas, distance: float, fill):
    segment = canvas.create_arc(
        20, 20, 700, 700,
        start=360-distance,
        extent=-SEGMENT,
        fill=fill,
        width=5,
    )
    return segment
