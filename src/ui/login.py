import tkinter as tk
import sqlite3
from tkinter import Frame

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 15
Y = 10

class LoginView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.minsize(315, 260)
        self.window.geometry('315x260')
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)

        frame = Frame(self.window)

        frame.grid(row=0, column=0, sticky="NESW")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(frame, text="Login or Create Username")
        self.label.grid(column=0, row=0, padx=X, pady=Y)

        self.input_username = tk.Entry(frame, width=30)
        self.input_username.grid(column=0, row=1, padx=X, pady=Y)

        self.btn_play = tk.Button(
            frame,
            text="Play",
            width=10,
            command=self.check_for_usernames,
        )
        self.btn_play.grid(column=0, row=3, padx=X, pady=Y)

        self.btn_users = tk.Button(
            frame,
            text="Users",
            width=10,
            command=self.list_all_users,
        )
        self.btn_users.grid(column=0, row=4, padx=X, pady=Y)

        self.window.mainloop()

    def destroy_login_view(self):
        self.window.destroy()

    def check_for_usernames(self):
        users = []
        for user in db.execute("SELECT username FROM Users").fetchall():
            users.append(f"{user['username']}")
        if len(self.input_username.get()) < 3:
            tk.messagebox.showinfo('Invalid Username','Username should be 3 or more characters long.')
        elif self.input_username.get() in users:
            tk.messagebox.showinfo('Logged in!',f'Welcome back, {self.input_username.get()}!')
            self.destroy_login_view()
        else:
            db.execute("INSERT INTO Users (username, password) VALUES (?,?)", (self.input_username.get(), ""))
            tk.messagebox.showinfo('Username Created',f'Nice to meet you, {self.input_username.get()}!')
            self.destroy_login_view()

    def list_all_users(self):
        users = []
        for user in db.execute("SELECT username FROM Users").fetchall():
            users.append(f"{user['username']}")
        if len(users) > 0:
            userlist = '\n'.join(sorted(users))
            tk.messagebox.showinfo('Users',f'List of users on this device: \n\n{userlist}')
        else:
            tk.messagebox.showinfo('Users','There are currently no users on this device.')

    def bind_key_to_button(self, window):
        window.widget.invoke()
