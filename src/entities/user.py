class User:
    """Class that describes an individual user.

    Attributes:
        username (str): The user's username.
        password (str): The user's password.
        login_status (int): The user's login status.
    """

    def __init__(self, username: str, password: str, login_status=0):
        """Class constructor that initializes a new user.

        Args:
            username (str): The user's username.
            password (str): The user's password.
            login_status (int): The user's login status.
        """

        self.username = username
        self.password = password
        self.login_status = login_status
