from typing import List

from objects.object import Object


class Stage:
    #TODO, debug mode with borders around stages
    def __init__(self, start_x: int, width: int, obstacles: List[Object]):
        self.width = width
        self.start_x = start_x
        self.obstacles = obstacles

        for obstacle in self.obstacles:
            obstacle.move_right_instant(self.start_x)