class programer:
    
    def __init__(self, salary, hours):
        self.salary = salary
        self.hours = hours
        
    def __del__(self):
       print("oof, " + str(self.salary) + ", " + str(self.hours))
   
    def compare(self, y):
        if self.salary < y.salary:
            return self
        elif self.salary > y.salary:
            return y
        elif self.salary == y.salary:
            if self.hours > y.hours:
                return self
            else:
                return y
            

p1 = programer(25000,5)
p2 = programer(25500, 5)
print(p1.compare(p2))
        
        
        
	