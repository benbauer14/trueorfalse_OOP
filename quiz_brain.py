class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):

        while self.question_number < len(self.question_list):
            currentQuestion = self.question_list[self.question_number]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {currentQuestion.text} (True/False:")
            if(answer == currentQuestion.answer):
                self.score +=1
                print(f"Correct!!! {self.score}/{self.question_number} ")
            else:
                print(f"Inorrect!!! {self.score}/{self.question_number} ")
