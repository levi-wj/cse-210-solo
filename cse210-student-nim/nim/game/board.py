import random

class Board:
    def __init__(self) -> None:
        self._piles = []
        self._prepare()
    
    def apply(self, move):
        self._piles[move.get_pile()] -= move.get_stones()

    def is_empty(self):
        for pile in self._piles:
           if pile > 0:
               return False

        return True

    def to_string(self):
        text =  "\n-------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n-------------------"
        return text

    def _prepare(self):
       for pile in range(random.randint(2, 5)):
           self._piles.append(random.randint(1, 9))