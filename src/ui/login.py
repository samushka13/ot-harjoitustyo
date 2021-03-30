import tkinter as tk

class LoginView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.geometry("800x600")

        self.greeting = tk.Label(text="Hello, Samushka")
        tk.Label.pack(self.greeting)

        self.label = tk.Label(
            text="Login",
            height=5,
        )

        tk.Label.pack(self.label)

        input_username = tk.Entry()
        input_username.pack()

        # if input_username.get() == "Samushka":
        #     pass
        # else:
        #     raise ValueError('This username does not exist. Please try another.')

        self.label = tk.Label(
            text="Create Username",
            height=5,
        )

        tk.Label.pack(self.label)

        create_username = tk.Entry()
        create_username.pack()

        self.btn_play = tk.Button(
            self.window,
            text="Play",
            width=30,
            height=15,
            command=self.destroy_login_view,
        )
        self.btn_play.pack()

        self.window.mainloop()

    def destroy_login_view(self):
        self.window.destroy()
