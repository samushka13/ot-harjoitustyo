from ui.widgets import get_board_segment
from ui.stylings import BACKGROUND

class GameBoard:
    """Class that describes a game board entity.

    Attributes:
        service (class): The current services class.
        window (window): A tkinter window.
        canvas (widget): A tkinter canvas widget.
        category_colors (list): List of category colors.
    """
    def __init__(self, service, window, canvas, category_colors):
        """Class constructor that initiates new game board for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            category_colors (list): List of category colors.
        """
        self.service = service
        self.window = window
        self.canvas = canvas
        self.size = self.service.get_board_size()
        self.categories = self.service.get_categories()[1:]
        self.category_colors = category_colors[1:]
        self.special_category = self.service.get_categories()[0]
        self.special_color = category_colors[0]
        self._build_board()

    def _build_board(self):
        """Builds the game board segments based on values
        returned by other methods in this and the services class.
        """
        segments = self.service.calculate_number_of_segments()
        segment = self.service.calculate_segment_size()
        category_segments = self.service.list_all_category_segments()
        self._assign_categories_to_segment(segment, segments, category_segments)
        self._build_center_circle()

    def _assign_categories_to_segment(self, segment: float, segments: int, categories: list):
        """Places the selected categories on the correct segments on the game board.

        Args:
            segment (float): The size of an individual segment.
            segments (int): The number of segments.
            categories (list): A nested list of integers of the places of categories on the board.
        """
        distance = 0
        segment_counter = 0
        while segment_counter < segments:
            if segment_counter == 0:
                get_board_segment(self.canvas, distance, segment, self.special_color)
            if segment_counter in categories[0]:
                get_board_segment(self.canvas, distance, segment, self.category_colors[0])
            i = 0
            while len(self.categories) >= i+2:
                if segment_counter in categories[i+1]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[i+1])
                i += 1
                if i == 11:
                    i = 0
            distance += segment
            segment_counter += 1

    def _build_center_circle(self):
        """Draws a circle at the center of the canvas
        to help form visible shape of the game board.
        """
        self.canvas.create_oval(100, 100, 620, 620, fill=BACKGROUND, width=4)
