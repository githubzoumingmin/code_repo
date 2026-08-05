from random import randint
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self,new_num_sides=None):
        if new_num_sides is not None:
            self.num_sides = new_num_sides
        for i in range(20):
            print(randint(1, self.num_sides))