import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]


user = int(input(
    f"choose 0 for rock {rock}, choose 1 for paper {paper} or choose 2 for scissors {scissors} pick: "))

cpu = random.randint(0, 2)


if user == 0 and cpu == 1:
    print(rps[user])
    print(rps[cpu])
    print("lose")
elif user == 1 and cpu == 0:
    print(rps[user])
    print(rps[cpu])
    print("win")
elif user == 0 and cpu == 2:
    print(rps[user])
    print(rps[cpu])
    print("win")
elif user == 2 and cpu == 0:
    print(rps[user])
    print(rps[cpu])
    print("lose")
elif user == 0 and cpu == 0:
    print(rps[user])
    print(rps[cpu])
    print("tie")
elif user == 1 and cpu == 2:
    print(rps[user])
    print(rps[cpu])
    print("lose")
elif user == 2 and cpu == 1:
    print(rps[user])
    print(rps[cpu])
    print("win")
elif user == 1 and cpu == 1:
    print(rps[user])
    print(rps[cpu])
    print("tie")
else:
    print(rps[user])
    print(rps[cpu])
    print("tie")
