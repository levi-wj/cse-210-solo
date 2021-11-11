from game.action import Action

class DrawActorsAction(Action):
    def __init__(self, outputservice):
        self._outputservice = outputservice

    def execute(self, cast):
        self._outputservice.clear_screen()
        for member in cast:
            for member in cast[member]:
                self._outputservice.draw_actor(member)
        self._outputservice.flush_buffer()