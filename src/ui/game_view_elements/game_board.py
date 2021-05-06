from ui.widgets import board_segment
from ui.stylings import BACKGROUND

class GameBoard:
    """Class that describes a game board entity.

    Attributes:
        service (class): The current services class entity.
        canvas (widget): A tkinter canvas widget.
        category_colors (list): List of category colors.
    """

    def __init__(self, service, canvas, category_colors):
        """Class constructor that initializes new game board for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class entity.
            canvas (widget): A tkinter canvas widget.
            category_colors (list): List of category colors.
        """

        self.service = service
        self.canvas = canvas
        self.colors = category_colors
        self.categories = self.service.categories
        self.segments = self.service.calculate_number_of_segments()
        self.size = self.service.calculate_segment_size()
        self.category_places = self.service.list_all_category_segments()
        self._draw_segments()
        self._draw_center()

    def _draw_segments(self):
        """Draws the segments dynamically based on given information.
        The unique category is drawn first, then the rest are drawn by a nested loop."""

        board_segment(self.canvas, 0, self.size, self.colors[0])
        segment_counter = 1
        while segment_counter < self.segments:
            i = 0
            while len(self.categories[1:]) >= i+1:
                if segment_counter in self.category_places[i]:
                    distance = self.size * segment_counter
                    board_segment(self.canvas, distance, self.size, self.colors[i+1])
                i += 1
            segment_counter += 1

    def _draw_center(self):
        """Draws a circle onto the center of the canvas
        to help form the game board's shape."""

        self.canvas.create_oval(100, 100, 620, 620, fill=BACKGROUND, width=4)
