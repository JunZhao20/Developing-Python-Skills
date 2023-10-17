name1 = input("Enter your name 1: ")
name2 = input("Enter your name 2: ")

love = ['l', 'o', 'v', 'e']
true = ['t', 'r', 'u', 'e']
Lcount = 0
Tcount = 0

for i in name1.lower():
    if i in true:
        Tcount += 1
        if i in love:
            Lcount += 1


for x in name2.lower():
    if x in true:
        Tcount += 1
        if x in love:
            Lcount += 1


Lcount = str(Lcount)
Tcount = str(Tcount)

total = str(Tcount+Lcount)

totalInt = int(total)

if totalInt < 10 or totalInt > 90:
    print(f"Your score is {totalInt} , you go together like coke and mentos.")
elif totalInt in range(40, 51):
    print(f"Your score is {totalInt} , you'll be alright.")
else:
    print(f"Your score is {totalInt}")
