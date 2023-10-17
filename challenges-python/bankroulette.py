import random

string_names = input("Enter name for roulette ('Format - ', ''): ")

split = string_names.split(", ")

names = []

for i in split:
    names.append(i)

roulette = random.randint(0, len(names))

print(f"{names[roulette]} will have to pay the bill")
