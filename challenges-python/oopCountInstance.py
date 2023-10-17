class User:

    lst = []

    def __init__(self, name):
        self.name = name
        self.lst.append(self.name)

    @classmethod
    def count_user(cls):
        return len(cls.lst)


u1 = User('bob12')

u2 = User('sam12')

print(User.count_user())
