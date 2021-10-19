import random

class Hider:
    """ The Hider class handles the distance between the hider and the seeker
    
    Stereotype:
        
    Attributes:
        location (int): where I am hiding
        distance (int): how close are you
        get_hint (string): returns warmer or colder
        watch (int): gets the distance between the hider and seeker
    """

    def __init__(self):
        self.location = random.randint(0, 1000)
        self.distance = [0, 0]

    def get_hint(self):
        if self.distance[1] == 0:
            return 'Oh! You found me!'
        elif self.distance[0] > self.distance[1]:
            return 'Getting warmer!'
        else:
            return 'Getting colder...'

    def watch(self, seekerpos):
        distance = abs(self.location - seekerpos)
        self.distance = [self.distance[1], distance]
        return self.distance