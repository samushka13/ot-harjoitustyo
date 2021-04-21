class User:
    """Class that describes an individual user.

    Attributes:
        username: String value of the user's username.
        password: String value of the user's password.
        login_status: An integer value of the user's login status.
    """

    def __init__(self, username: str, password: str, login_status=0):
        """Class constructor that initiates a new user.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
            login_status: An integer value of the user's login status.
        """

        self.username = username
        self.password = password
        self.login_status = login_status
