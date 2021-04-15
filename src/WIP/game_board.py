from ui.widgets import get_board_segment
from ui.stylings import BACKGROUND

class GameBoard:
    def __init__(self, window, canvas, size: int, categories: list, category_colors: list):
        self.window = window
        self.canvas = canvas
        self.size = size
        self.categories = categories[1:]
        self.category_colors = category_colors[1:]
        self.special_category = categories[0]
        self.special_color = category_colors[0]

    def _calculate_segments(self):
        segments = len(self.categories)*self.size+1
        segment = 360/segments
        return segment, segments

    def _list_all_category_segments(self):
        all_category_segments = []
        i = 0
        while i < len(self.categories):
            j = 0
            k = 1 + i
            category_segments = []
            while j <= self.size:
                category_segments.append(k)
                k += len(self.categories)
                j += 1
            i += 1
            all_category_segments.append(category_segments)
        return all_category_segments

    def _assign_categories_to_segment(
        self, segment: float, segments: int, all_category_segments: list):
        distance = 0
        segment_counter = 0
        while segment_counter < segments:
            if segment_counter == 0:
                get_board_segment(self.canvas, distance, segment, self.special_color)
            if segment_counter in all_category_segments[0]:
                get_board_segment(self.canvas, distance, segment, self.category_colors[0])
            if len(self.categories) >= 2:
                if segment_counter in all_category_segments[1]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[1])
            if len(self.categories) >= 3:
                if segment_counter in all_category_segments[2]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[2])
            if len(self.categories) >= 4:
                if segment_counter in all_category_segments[3]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[3])
            if len(self.categories) >= 5:
                if segment_counter in all_category_segments[4]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[4])
            if len(self.categories) >= 6:
                if segment_counter in all_category_segments[5]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[5])
            if len(self.categories) >= 7:
                if segment_counter in all_category_segments[6]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[6])
            if len(self.categories) >= 8:
                if segment_counter in all_category_segments[7]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[7])
            if len(self.categories) >= 9:
                if segment_counter in all_category_segments[8]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[8])
            if len(self.categories) >= 10:
                if segment_counter in all_category_segments[9]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[9])
            if len(self.categories) >= 11:
                if segment_counter in all_category_segments[10]:
                    get_board_segment(self.canvas, distance, segment, self.category_colors[10])
            distance += segment
            segment_counter += 1

    def build(self):
        segment = self._calculate_segments()[0]
        segments = self._calculate_segments()[1]
        all_segments = self._list_all_category_segments()
        self._assign_categories_to_segment(segment, segments, all_segments)
        # ----------------------------------------------------------
        # A graphic hack that helps form the game board's shape:
        # ----------------------------------------------------------
        self.canvas.create_oval(100, 100, 620, 620, fill=BACKGROUND, width=4)
