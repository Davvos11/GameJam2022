from objects.pipe import Pipe
from stages.stage import Stage


class TestStage(Stage):
    def __init__(self, start_x: int, ground_y):
        obstacles = [
            Pipe({'x': 0, 'y': 0})
        ]
        super().__init__(start_x, width=500, obstacles=obstacles, ground_y=ground_y)
