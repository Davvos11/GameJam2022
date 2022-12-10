from typing import List

from objects.grass import Grass
from stages.stage import Stage


class HillStage(Stage):
    def __init__(self, start_x: int):
        obstacles = [
            Grass({'x': 100, 'y': 500}, 550),
            Grass({'x': 200, 'y': 400}, 400),
            Grass({'x': 300, 'y': 300}, 200),
        ]
        super().__init__(start_x, width=400, obstacles=obstacles)
