from timer import countdown
import time


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        total_questions = len(self.questions)

        for index, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {index}: {q['question']}")

            for i, option in enumerate(q["options"], start=1):
                print(f"{i}. {option}")

            print("\nYou have 10 seconds to answer.")
            countdown(10)

            try:
                user_choice = int(input("\nEnter option number: "))
                selected_answer = q["options"][user_choice - 1]
            except (ValueError, IndexError):
                print("Invalid input.")
                continue

            if selected_answer == q["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")

            time.sleep(1)

        self.show_result(total_questions)

    def show_result(self, total):
        print("\n===============================")
        print("          QUIZ RESULT")
        print("===============================")

        print(f"Score: {self.score}/{total}")

        percentage = (self.score / total) * 100

        if percentage >= 80:
            print("Performance: Excellent")
        elif percentage >= 50:
            print("Performance: Good")
        else:
            print("Performance: Needs Improvement")

        print("===============================\n")