# Student Grade Evaluation Program - Modified Version

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / 5

if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Average Marks: {average:.2f}")
print("Grade:", grade)