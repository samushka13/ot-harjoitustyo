from tkinter import ttk
from services.database_operations import get_categories
from entities.settings import NUMBER_OF_PLAYERS, BOARD_SIZE_NAMES
from ui.stylings import X, Y

def get_players_combobox(window):
    players_combobox = ttk.Combobox(window, width=30)
    values = players_combobox['values'] = NUMBER_OF_PLAYERS
    players_combobox.state(['readonly'])
    players_combobox.set(values[0])
    players_combobox.grid(column=0, row=2, columnspan=2, padx=X, pady=Y)
    return players_combobox, players_combobox.focus()

def get_board_size_combobox(window):
    board_size_combobox = ttk.Combobox(window, width=30)
    board_size_combobox['values'] = BOARD_SIZE_NAMES
    board_size_combobox.state(['readonly'])
    board_size_combobox.set(BOARD_SIZE_NAMES[2])
    board_size_combobox.grid(column=0, row=4, columnspan=2, padx=X, pady=Y)
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
        category_combobox.grid(column=0, row=6+i, columnspan=2, padx=X, pady=Y)
        comboboxes.append(category_combobox)
        i += 1
    return comboboxes
