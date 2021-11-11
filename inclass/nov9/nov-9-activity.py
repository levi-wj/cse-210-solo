from random import randint
from time import sleep

class Entity:
    def __init__(self, output, output_chance):
        self._output = output
        self._output_chance = output_chance
    
    def output(self):
        if randint(1, self._output_chance) == 1:
            print(self._output)

class Dog(Entity):
    def __init__(self):
        super().__init__('Woof!', 2)

class Cat(Entity):
    def __init__(self):
        super().__init__('meeeeeeeeeeeeeeeeowwwwww', 3)

class Pig(Entity):
    def __init__(self):
        super().__init__('oink oink', 3)

class Anakin(Entity):
    def __init__(self):
        super().__init__('i don\'t like sand', 2)

class Herd(Entity):
    def __init__(self, creatures):
        self.creatures = creatures

flock = Herd([Dog(), Dog(), Cat(), Cat(), Anakin(), Pig(), Pig()])

while True:
    for x in flock.creatures:
        x.output()
    sleep(.5)