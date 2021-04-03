import tkinter as tk
import sqlite3
from tkinter import Frame

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 20
Y = 0

class LoginView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.minsize(360,360)
        self.window.geometry('360x360')
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)

        frame = Frame(self.window)
        frame.grid(row=0, column=0, sticky="NESW")
        for i in (0,5):
            frame.grid_rowconfigure(i, weight=2)
        for i in (1,2,3,4,6):
            frame.grid_rowconfigure(i, weight=1)
        for i in (0,1):
            frame.grid_columnconfigure(i, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(frame, text="Login or Create Username", font=('Helvetica', 16, 'bold'))
        self.label.grid(column=0, row=0, columnspan=2, padx=X, pady=Y)

        label = tk.Label(frame, text="Username")
        label.grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.input_username = tk.Entry(frame, width=30)
        self.input_username.grid(column=0, row=2, columnspan=2, padx=X, pady=Y)

        label = tk.Label(frame, text="Password")
        label.grid(column=0, row=3, padx=X, columnspan=2, pady=Y)

        self.input_password = tk.Entry(frame, width=30, show="*")
        self.input_password.grid(column=0, row=4, columnspan=2, padx=X, pady=Y)

        self.btn_proceed = tk.Button(
            frame,
            text="Proceed",
            width=10,
            command=self.check_for_usernames,
        )
        self.btn_proceed.grid(column=0, row=5, padx=X, pady=Y)

        self.btn_users = tk.Button(
            frame,
            text="Users",
            width=10,
            command=self.list_all_users,
        )
        self.btn_users.grid(column=1, row=5, padx=X, pady=Y)

        self.window.mainloop()

    def destroy_login_view(self):
        self.window.destroy()

    def check_for_usernames(self):
        credentials = []
        for row in db.execute("SELECT username, password FROM Users").fetchall():
            credentials.append((row['username'],row['password']))
        if len(self.input_username.get()) < 3:
            tk.messagebox.showinfo('Invalid Username','Username should be 3 or more characters long.')
        elif (self.input_username.get(),self.input_password.get()) in credentials:
            tk.messagebox.showinfo('Logged in!',f'Welcome back, {self.input_username.get()}!')
            self.destroy_login_view()
        else:
            if [item for item in credentials if item[0] == self.input_username.get()]:
                tk.messagebox.showinfo('Login Error',"Username and password don't match.")
            else:
                db.execute("INSERT INTO Users (username, password) VALUES (?,?)", (self.input_username.get(), self.input_password.get()))
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
