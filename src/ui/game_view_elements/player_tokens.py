import tkinter as tk

class PlayerTokens:
    """Class that describes the player tokens entity.

    Attributes:
        service (class): The current services class.
        canvas (widget): A tkinter canvas widget.
        player_colors (list): List of player colors.
    """
    def __init__(self, service, canvas, player_colors):
        """Class constructor that initiates new tokens for the game view window.
        The tokens are drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            canvas (widget): A tkinter canvas widget.
            player_colors (list): List of player colors.
        """
        self.service = service
        self.canvas = canvas
        self.players = self.service.get_players()
        self.player_colors = player_colors
        self.size = self.service.calculate_segment_size()
        self.tokens = []
        self.starting_positions = [360, 360, 360, 360, 360, 360]
        self._build_tokens()

    def _build_tokens(self):
        """Builds the player tokens onto the game board.
        """
        player_index = 0
        xy_increase = 0
        while player_index < len(self.players):
            token = self.canvas.create_arc(
                115+xy_increase, 115+xy_increase, 605-xy_increase, 605-xy_increase,
                start=self.starting_positions[player_index],
                extent=-self.size,
                outline=self.player_colors[player_index],
                width=10,
                style=tk.ARC,
            )
            self.tokens.append(token)
            player_index += 1
            xy_increase += 15

    def move_token(self, player, number):
        """Removes the old token widget and draws a new one.

        Args:
            player (int): The index of the current player.
            number (int): The number of segments the token travels.
        """
        new_position = self.starting_positions[player]-self.size*(number)
        self.canvas.delete(self.tokens[player])
        self.starting_positions[player] = new_position
        token = self.canvas.create_arc(
            115+(player*15), 115+(player*15), 605-(player*15), 605-(player*15),
            start=new_position,
            extent=-self.size,
            outline=self.player_colors[player],
            width=10,
            style=tk.ARC,
        )
        self.service.count_laps(player, self.starting_positions, new_position)
        self.tokens[player] = token
