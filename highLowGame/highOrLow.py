import game_data as gd
import random as rd


def high_low():
    lose = False
    score = 0

    while lose != True:

        A = rd.choice(gd.data)

        B = rd.choice(gd.data)

        print(
            f"Compare A: {A['follower_count']}, {A['name']}, {A['description']}, from {A['country']}.\n")
        print("VS\n")
        print(
            f"Compare b: {B['follower_count']}, {B['name']}, {B['description']}, from {B['country']}.")

        pick = input("Who has the most followers (A or B)?: ").upper()

        # if A is picked and A is more than B
        if pick == 'A' and A['follower_count'] > B['follower_count']:

            score += 1
            print(f"correct {score}")

        # if B is picked and B is more than A
        elif pick == 'B' and B['follower_count'] > A['follower_count']:
            A = B
            score += 1
            print(f"correct {score}")

        # if A is picked and A is equal to B
        elif pick == 'A' and A['follower_count'] == B['follower_count']:
            A = A
            score += 1
            print(f"correct {score}")

        # if ABis picked and B is equal to A
        elif pick == 'B' and B['follower_count'] == A['follower_count']:
            A = B
            score += 1
            print(f"correct {score}")

        else:
            lose = True
            print(f"You are wrong! Score: {score}.")


high_low()
