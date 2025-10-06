# Student Grade Evaluation Program

marks = int(input("Enter marks of the student: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'Fail'

print("Grade:", grade)
