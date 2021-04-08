import tkinter as tk
from tkinter import Frame
from settings import SettingsView
from ui.stylings import LOGIN_WINDOW_NAME, LOGIN_WINDOW_SIZE, BACKGROUND, TITLE_FONT, X, Y
from services.database_connection import db
from services.database_operations import add_user, get_credentials, get_users

class LoginView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(LOGIN_WINDOW_NAME)
        self.window.geometry(LOGIN_WINDOW_SIZE)
        self.window.resizable(False, False)
        self.window.configure(bg=BACKGROUND)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)
        self.window.focus()
        
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

        self.label = tk.Label(frame, text="Login or Create Username", font=TITLE_FONT)
        self.label.grid(column=0, row=0, columnspan=2, padx=X, pady=Y)

        label = tk.Label(frame, text="Username")
        label.grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.input_username = tk.Entry(frame, width=30)
        self.input_username.grid(column=0, row=2, columnspan=2, padx=X, pady=Y)
        self.input_username.focus()

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
            command=self.list_of_users,
        )
        self.btn_users.grid(column=1, row=5, padx=X, pady=Y)

        self.window.mainloop()

    def open_settings_view(self):
        self.window.destroy()
        SettingsView()

    def check_for_usernames(self):
        credentials = get_credentials()
        if len(self.input_username.get()) < 3:
            tk.messagebox.showinfo('Invalid Username','Username should be 3 or more characters long.')
            self.window.focus()
            self.input_username.focus()
        elif (self.input_username.get(),self.input_password.get()) in credentials:
            tk.messagebox.showinfo('Logged in!',f'Welcome back, {self.input_username.get()}!')
            self.open_settings_view()
        else:
            if [item for item in credentials if item[0] == self.input_username.get()]:
                tk.messagebox.showinfo('Login Error',"Username and password don't match.")
                self.window.focus()
                self.input_username.focus()
            else:
                add_user(self.input_username.get(), self.input_password.get())
                tk.messagebox.showinfo('Username Created',f'Nice to meet you, {self.input_username.get()}!')
                self.open_settings_view()

    def list_of_users(self):
        users = get_users()
        if len(users) > 0:
            users_list = '\n'.join(sorted(users))
            info = tk.messagebox.showinfo('Users',f'List of users on this device: \n\n{users_list}')
        else:
            info = tk.messagebox.showinfo('Users','There are currently no users on this device.')
        if info == 'ok':
            self.window.focus()
            self.input_username.focus()

    def bind_key_to_button(self, window):
        window.widget.invoke()
