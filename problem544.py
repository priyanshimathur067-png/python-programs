
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Exam:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def start_exam(self):
        score = 0

        for q in self.questions:
            print(q.question)
            user_answer = input("Enter answer: ")

            if user_answer.lower() == q.answer.lower():
                score += 1

        print("Final Score:", score, "/", len(self.questions))


exam = Exam()

exam.add_question(Question("Capital of India?", "Delhi"))
exam.add_question(Question("Python is a language?", "Yes"))
exam.add_question(Question("5 + 5?", "10"))

exam.start_exam()
