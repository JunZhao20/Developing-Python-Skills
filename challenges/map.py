
map = [['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']]
print(f"{map[0]}\n{map[1]}\n{map[2]}")

user = list((input("Input coordinate to place X: ")))

userInt = [eval(i) for i in user]

num = []

for i in userInt:
    if i > 0:
        i -= 1
        num.append(int(i))


map[num[1]][num[0]] = 'X'

print(f"{map[0]}\n{map[1]}\n{map[2]}")
