class player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is {self.age} years old."

    def get_height(self):
        return f"{self.name} is {self.height}cm tall."

    def get_weight(self):
        return f"{self.name} is {self.weight}kg."


player1 = player('bob', 19, 190, 85)

print(player1.get_age())
