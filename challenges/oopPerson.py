class Person:
    
    def __init__(self, name, like, dislike):
        self.name = name
        self.like = like
        self.dislike = dislike
    
    def taste(self, food):
        if food in self.like:
            return f"{self.name} likes {food}"
        elif food in self.dislike:
            return f"{self.name} dislikes {food}"
        else:
            return f"{self.name} eats {food}"
            

p1 = Person('sam', ['ice'], ['tie'])

print(p1.taste('pie'))

