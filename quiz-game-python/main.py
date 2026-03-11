from quiz_logic import QuizGame
from questions import question_data


def main():
    print("\n===============================")
    print("      PYTHON QUIZ GAME")
    print("===============================\n")

    quiz = QuizGame(question_data)
    quiz.start_quiz()


if __name__ == "__main__":
    main()