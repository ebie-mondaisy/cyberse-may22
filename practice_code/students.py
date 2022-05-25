class Student:

    def __init__(self, name, age, class_= "student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def result(self, score1, score2, score3):
        return f"{self.name}'s average score is: " + str((score1 + score2 + score3)/3)


#score = input("Enter score: ")

s1 = Student("Mandy", 23, "Nano Tech")
s2 = Student("Guhlinduh", 21, "Rocket Science")
score1 = 67
score2 = 89
score3 = 76
print(s1.result(score1, score2, score3))
