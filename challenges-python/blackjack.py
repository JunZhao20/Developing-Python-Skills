import random
"""
cards = {
    "Ace": 11,
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "king": 10,
    "Queen": 10
}
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def bust_win(player, cpu):
    if cpu < 21 and cpu > player:
        print("lose")
    elif player < 21 and player > cpu:
        print("win")


def blackjack():
    cpu = 0
    player = 0
    start = input("Do you want to play blackjack y or n?: ")

    while start != 'n':
        playerDeck = random.choices(cards, k=2)
        player += sum(playerDeck)
        print(f"Player deck: {playerDeck, player}")

        cpuDeck = random.choices(cards, k=2)
        cpu += sum(cpuDeck)
        print(f"Cpu deck {cpuDeck, cpu}")

        if cpu == 21:
            print("lose")

        elif player == 21:
            player("win")

        elif player == 21 and cpu == 21:
            print("draw")

        player_action = input("Do you want to hit or stand (h or s)?: ")
        if player_action == "h":
            playerDeck.append(random.choice(cards))
            player = sum(playerDeck)
            print(playerDeck, player)
            if player > 21:
                print("lose")
                break
            elif player == 21:
                print("win")
                break
            elif player == 21 and cpu == 21:
                print("draw")
                break

            player_action = input("Do you want to hit or stand (h or s)?: ")

            while cpu < 21:
                cpuDeck.append(random.choice(cards))
                cpu = sum(cpuDeck)
                if cpu > 21:
                    print("win")
                    print(f"Player deck: {playerDeck, player}")
                    print(f"Cpu deck {cpuDeck, cpu}")

        elif player_action == "s":
            while cpu < 21:
                cpuDeck.append(random.choice(cards))
                cpu = sum(cpuDeck)
                bust_win(player, cpu)
            print(f"Player deck: {playerDeck, player}")
            print(f"Cpu deck {cpuDeck, cpu}")

        cpu = 0
        player = 0

        start = input("Do you want to play blackjack y or n?: ")


blackjack()
