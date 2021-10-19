import random

'''
The thrower class handles generating the random values of the dice
It also handles assessing the value of the current dice
'''
class Thrower:
    def __init__(self):
       self.dice = []
       self.num_throws = 0 

    def can_throw(self):
        return self.num_throws == 0 or self.dice.count(1) > 0 or self.dice.count(5) > 0

    def get_points(self):
        return (self.dice.count(1) * 100) + (self.dice.count(5) * 50)

    def throw_dice(self):
        self.dice = []
        for i in range(0, 5):
            self.dice.append(random.randint(1, 6))
        self.num_throws += 1
