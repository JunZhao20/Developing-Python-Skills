
student_scores = {
    'Harry': 72,
    'Ron': 60,
    'Hermione': 99,
    'Draco': 80,
    'Neville': 9
}

for i in student_scores:
    if student_scores[i] in range(91, 101):
        student_scores[i] = "Outstanding"
    elif student_scores[i] in range(81, 91):
        student_scores[i] = "Exceeds Expectations"
    elif student_scores[i] in range(71, 81):
        student_scores[i] = "Acceptable"
    else:
        student_scores[i] = "Fail"

print(student_scores)
