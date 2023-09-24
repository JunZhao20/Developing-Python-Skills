import random


def hint(guess, num):
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")


def guess_game():
    win = False
    while win != True:
        num = random.randint(1, 101)
        difficulty = input("Type difficulty 'Easy' or 'Hard': ")
        difficulty = difficulty.lower()
        if difficulty == "easy":
            lives = 10
            print(f"You have {lives} lives")
            guess = int(input("what is your guess? "))
            while guess != num:
                hint(guess, num)
                if guess != num:
                    lives -= 1
                    if lives < 1:
                        print("You're out of attempts")
                        guess_game()
                    print(lives)
                    guess = int(input("what is your guess? "))
                else:
                    win = True
                    print("Your correct")

        elif difficulty == "hard":
            lives = 5
            print(f"You have {lives} lives")
            guess = int(input("what is your guess? "))
            while guess != num:
                hint(guess, num)
                if guess != num:
                    lives -= 1
                    if lives < 1:
                        print("You're out of attempts")
                        guess_game()
                    print(lives)
                    guess = int(input("what is your guess? "))

                else:
                    win = True
                    print("Your correct")


guess_game()
