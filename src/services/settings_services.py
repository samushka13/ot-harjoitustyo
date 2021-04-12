class SettingsServices():
    def __init__(self, current_user):
        self.current_user = current_user

    def get_default_players(self):
        default_players = [
            f"{self.current_user}",
            "Player 2",
            "Player 3",
            "Player 4",
            "Player 5",
            "Player 6",
        ]
        return default_players

    def get_default_player_colors(self):
        default_player_colors = [
            "red",
            "brown",
            "green",
            "purple",
            "orange",
            "blue",
        ]
        return default_player_colors

    def get_default_board_sizes(self):
        board_sizes = [
            ("Tiny (least difficult)", 1),
            ("Small", 3),
            ("Medium", 5),
            ("Large", 7),
            ("Insane", 9),
            ("The Ultimate Challenge", 30)
        ]
        return board_sizes

    def get_default_category_colors(self):
        category_colors = [
            "black",
            "red",
            "gold",
            "green",
            "purple",
            "orange",
            "blue",
            "grey",
            "brown",
            "pink",
            "magenta",
            "turquoise",
        ]
        return category_colors

    def get_default_difficulties(self):
        difficulty_names = [
            "Easy",
            "Intermediate",
            "Advanced Triviliast"
        ]
        return difficulty_names
