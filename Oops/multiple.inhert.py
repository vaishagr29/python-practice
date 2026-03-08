class Academics:
    def _init__(self, name, marks):
        self.name = name
        self.marks = marks
    def displayAcademics (self):
        print(f"Name: {self.name}, Marks: {self.marks}")
class Sports:
    def __init__(self, score):
        self.score = score
    def displayScore(self):
        print(f"Score: {self.score}")

class Result (Academics, Sports):
    def __init__(self, name, marks, score):
        Academics._init_(self, name, marks)
        Sports._init__(self, score)
    def result(self):
        total = self.marks + self.score
        print("Result = ", total)


s1 = Result("Parth", 67,8)
s1.result()
s2 = Result("Kartik", 85,9)
s2.result()