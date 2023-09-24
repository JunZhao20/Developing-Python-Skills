
import random

randomInt = random.randint(0, 1)

user = input("Heads or Tails (H or T)? ")

if user == 'H':
    user = 0
    if user == randomInt:
        print("win")
    else:
        print('lose')

elif user == 'T':
    user = 1
    if user == randomInt:
        print("win")
    else:
        print('lose')
else:
    print('lose')
