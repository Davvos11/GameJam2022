from typing import List

from objects.object import Object
from objects.pipe import Pipe
from stages.stage import Stage


class TestStage(Stage):
    def __init__(self, start_x: int):
        obstacles = [
            Pipe({'x': 0, 'y': 200})
        ]
        super().__init__(start_x, width=100, obstacles=obstacles)
