from repositories.database_services import DatabaseServices
from ui.login_view import LoginView
from config import DATABASE_FILENAME

def main():
    """Runs the app by initiating a LoginView class entity
    with a DatabaseServices class entity as its attribute.
    The attribute (and the database filename) is passed on to services class entities,
    so they and the repositories never dictate which database ('real' or 'test') is used.
    This isn't the 'prettiest' solution, but it made testing setup very easy."""

    LoginView(DatabaseServices(DATABASE_FILENAME))

if __name__ == "__main__":
    main()
