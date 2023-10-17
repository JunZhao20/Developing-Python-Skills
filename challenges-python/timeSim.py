
class SimTime:
    
    def __init__(self):
        self.sim = 0
        
    def get(self):
        return self.sim
    
    def set_speed(self, new_speed):
        self.sim += new_speed
        return self.sim
    
    def update(self):
        pass

sim1 = SimTime()

print(sim1.get())