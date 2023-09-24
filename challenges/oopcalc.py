
class calc:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2


calc1 = calc(1, 2)
print(calc1.add())
