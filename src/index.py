from repositories.database_services import DatabaseServices
from ui.login_view import LoginView
from config import DATABASE_FILENAME

def main():
    """Runs the app by initiating a LoginView class
    with a DatabaseServices class as its attribute."""

    LoginView(DatabaseServices(DATABASE_FILENAME))

if __name__ == "__main__":
    main()
