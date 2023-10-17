class ones_threes_nines:

    def __init__(self, num):
        self.num = num

    def ones(self):
        count = 0
        if self.num >= 0:
            while self.num != 0:
                self.num -= 1
                count += 1
            else:
                return count
        
        return count

    def threes(self):
        count = 0
        if self.num >= 0:
            while self.num != 0:
                self.num -= 3
                count += 1
            else:
                return count
        
        return count

    def nines(self):
        count = 0
        if self.num >= 0:
            while self.num != 0:
                self.num -= 9
                count += 1
            else:
                return count
        
        return count
        


n1 = ones_threes_nines(10)

print(n1.nines())
