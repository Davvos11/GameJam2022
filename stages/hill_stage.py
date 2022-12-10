from typing import List

from objects.grass import Grass
from stages.stage import Stage


class HillStage(Stage):
    def __init__(self, start_x: int, ground_y):
        obstacles = [
            Grass({'x': 100, 'y': 0}, 550),
            Grass({'x': 200, 'y': 100}, 400),
            Grass({'x': 300, 'y': 200}, 200),
        ]
        super().__init__(start_x, width=400, obstacles=obstacles, ground_y=ground_y)
