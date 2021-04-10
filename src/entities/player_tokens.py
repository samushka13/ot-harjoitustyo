import tkinter as tk

class PlayerTokens:
    def __init__(self, canvas, players: list, colors: list, size: float):
        self.canvas = canvas
        self.players = players
        self.colors = colors
        self.size = size
        self.starting_positions = [360, 360, 360, 360, 360, 360, 360, 360]
        self.tokens = []

    def _build(self):
        player_index = 0
        xy_increase = 0
        while player_index < len(self.players):
            token = self.canvas.create_arc(
                115+xy_increase, 115+xy_increase, 605-xy_increase, 605-xy_increase,
                start=self.starting_positions[player_index],
                extent=-self.size,
                outline=self.colors[player_index],
                width=10,
                style=tk.ARC,
            )
            self.tokens.append(token)
            player_index += 1
            xy_increase += 15
        return self.tokens

    def move_token(self, player, number):
        new_position = self.starting_positions[player]-self.size*(number)
        self.canvas.delete(self.tokens[player])
        self.starting_positions[player] = new_position
        token = self.canvas.create_arc(
            115+(player*15), 115+(player*15), 605-(player*15), 605-(player*15),
            start=new_position,
            extent=-self.size,
            outline=self.colors[player],
            width=10,
            style=tk.ARC,
        )

        # This helps keep track of the token's position in terms of the category segments,
        # as elsewhere tokens and categories are matched by their 'start' arguments.

        if new_position >= 360:
            new_position -= 360

            # Statistiikkoja varten tähän voisi myös lisätä jonkun counterin,
            # joka kasvaa aina yhdellä, kun 360 tulee täyteen.

        self.tokens[player] = token
