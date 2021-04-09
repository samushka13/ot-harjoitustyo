import tkinter as tk


window = tk.Tk()
window.title('Trivioboros')
window.geometry('360x360')
window.resizable(False, False)

while True:
    view = input("Select mode: ")
    if view == "settings":
        window.geometry('720x720')
    if view == "login":
        window.geometry('360x360')
    if view == "":
        break

window.mainloop()
