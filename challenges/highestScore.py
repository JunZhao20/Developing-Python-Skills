student_scores = []

user = input("Input your list to check for the highest number: ")

user = user.split()

for u in user:
    u = int(u)
    student_scores.append(u)


num = student_scores[0]
for i in student_scores:
    if i > num:
        num = i

print(num)
