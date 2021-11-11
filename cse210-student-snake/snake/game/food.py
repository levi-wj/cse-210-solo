import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):
    def __init__(self):
        self._points = 1
        self._text = '@'
        self.reset()

    def get_position(self):
        return self.__position

    def get_points(self):
        return self._points
    
    def reset(self):
        self.__position = Point(random.randint(0, constants.MAX_X), random.randint(1, constants.MAX_Y - 1))
