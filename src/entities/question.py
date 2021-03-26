class Question:
    def __init__(self, category, question, answer):
        self.category = category
        self.question = question
        self.answer = answer

    def __str__(self):
        return str(f"{self.category}\n{self.question}\n{self.answer}")
