from typing import List

from objects.object import Object


class Stage:
    # TODO, debug mode with borders around stages
    def __init__(self, start_x: int, width: int, obstacles: List[Object], ground_y):
        self.width = width
        self.start_x = start_x
        self.obstacles = obstacles

        for obstacle in self.obstacles:
            # Obstacles should be corrected to the start x of the stage
            obstacle.rectangle.x += self.start_x

            # Obstacles should be inverted such that y = 0 is seen as the bottom
            obstacle.rectangle.y = ground_y - obstacle.height - obstacle.rectangle.y
