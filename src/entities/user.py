class User:
    """Class that describes an individual user.

    Attributes:
        username: String value of the user's username.
        password: String value of the user's password.
    """

    def __init__(self, username: str, password: str):
        """Class constructor that initiates a new user.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
        """

        self.username = username
        self.password = password
