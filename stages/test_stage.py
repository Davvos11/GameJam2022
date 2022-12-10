from objects.pipe import Pipe
from stages.stage import Stage


class TestStage(Stage):
    width = 500

    def __init__(self, start_x: int, ground_y):
        obstacles = [
            Pipe({'x': 0, 'y': 0})
        ]
        super().__init__(start_x, width=TestStage.width, obstacles=obstacles, ground_y=ground_y)
