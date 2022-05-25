'''
Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)
'''
def gradeCalc(hw, assess, finex):
    result = (hw + assess + finex) / 175 * 100
    return result

sname = input("Enter student's name: ")
hw = int(input("Enter the homework score: "))
assess = int(input("Enter the assessment score: "))
finex = int(input("Enter the exam score: "))
result = int(gradeCalc(hw, assess, finex))

if result >= 80:
    grade = "A*"
elif result >= 70:
    grade = "A"
elif result >= 60:
    grade = "B"
elif result >= 50:
    grade = "C"
elif result >= 40:
    grade = "D"
elif result >= 30:
    grade = "E"
else:
    grade = "U"

print(f"{sname}: \nGrade; {grade}, \nPercentage; {result}%")