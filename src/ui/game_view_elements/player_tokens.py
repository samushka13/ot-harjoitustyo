import tkinter as tk

class PlayerTokens:
    """Class that describes the player tokens entity.

    Attributes:
        service (class): The current services class.
        canvas (widget): A tkinter canvas widget.
        player_colors (list): List of player colors.
    """

    def __init__(self, service, canvas, player_colors):
        """Class constructor that initializes new tokens for the game view window.
        The tokens are drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            canvas (widget): A tkinter canvas widget.
            player_colors (list): List of player colors.
        """

        self.service = service
        self.canvas = canvas
        self.player_colors = player_colors
        self.players = self.service.players
        self.size = self.service.calculate_segment_size()
        self.tokens = []
        self._draw_tokens()

    def _draw_tokens(self):
        """Draws the player tokens onto the game board."""

        indent = 0
        for i in range(len(self.players)):
            token = self.canvas.create_arc(
                115+indent, 115+indent, 605-indent, 605-indent,
                start=self.service.player_positions_radii[i],
                extent=-self.size,
                outline=self.player_colors[i],
                width=10,
                style=tk.ARC,
            )
            self.tokens.append(token)
            indent += 15

    def move_token(self, player, new_position, starting_positions):
        """Removes the old token widget and draws a new one.

        Args:
            player (int): The index of the current player.
            new_position (int): The token's new position.
            starting_positions (list): The tokens' starting positions.
        """

        self.canvas.delete(self.tokens[player])
        starting_positions[player] = new_position
        token = self.canvas.create_arc(
            115+(player*15), 115+(player*15), 605-(player*15), 605-(player*15),
            start=new_position,
            extent=-self.size,
            outline=self.player_colors[player],
            width=10,
            style=tk.ARC,
        )
        self.tokens[player] = token
