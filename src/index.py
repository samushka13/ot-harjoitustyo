from ui.login_view import login_view


def main():
    """Runs the app by initiating a LoginView class entity
    and calling one of its methods to initialize an actual window."""

    login_view.initialize_window()

if __name__ == "__main__":
    main()
