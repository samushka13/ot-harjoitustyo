class Player:
    """Class that describes a player.

    Attributes:
        name (str): The player's name.
        color (str): The player's color.
        points (list): The player's category points as tuples of integer values.
        token_position_index (int): The token's position in terms of game board segments.
        token_position_radius (int): The token's position as a measure of radius.
    """

    def __init__(self, name, color, points, token_position_index, token_position_radius):
        """Class constructor that initializes a new user.

        Args:
            name (str): The player's name.
            color (str): The player's color.
            points (list): The player's category points as tuples of integer values.
            token_position_index (int): The token's position in terms of game board segments.
            token_position_radius (int): The token's position as a measure of radius.
        """

        self.name = name
        self.color = color
        self.points = points
        self.token_position_index = token_position_index
        self.token_position_radius = token_position_radius
