class Question:
    """Class that describes an individual question item.

    Attributes:
        user_id: An integer value of the user's id.
        category: String value of the item's category.
        difficulty: String value of the item's difficulty.
        question: String value of the item's question.
        answer: String value of the item's answer.
    """

    def __init__(self, user_id, category, difficulty, question, answer):
        """Class constructor that initiates a new question item.

        Args:
            user_id: An integer value of the user's id.
            category: String value of the item's category.
            difficulty: String value of the item's difficulty.
            question: String value of the item's question.
            answer: String value of the item's answer.
        """

        self.user_id = user_id
        self.category = category
        self.difficulty = difficulty
        self.question = question
        self.answer = answer
