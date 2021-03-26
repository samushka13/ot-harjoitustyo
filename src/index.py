from entities.question import Question
from entities.user import User

def main():
    user = User("samushka")
    question = Question("Computer Science", "What is 'python'?", "A programming language")
    print(user)
    print()
    print(question)

if __name__ == "__main__":
    main()
