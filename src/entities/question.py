class Question:
    """Class that describes an individual question item.

    Attributes:
        user_id (int): The user's id.
        category (str): The question item's category.
        difficulty (str): The question item's difficulty.
        question (str): The question item's question.
        answer (str): The question item's answer.
    """

    def __init__(self, user_id, category, difficulty, question, answer):
        """Class constructor that initializes a new question item.

        Args:
            user_id (int): The user's id.
            category (str): The question item's category.
            difficulty (str): The question item's difficulty.
            question (str): The question item's question.
            answer (str): The question item's answer.
        """

        self.user_id = user_id
        self.category = category
        self.difficulty = difficulty
        self.question = question
        self.answer = answer
