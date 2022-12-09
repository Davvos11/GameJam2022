from objects.pipe import Pipe
from stages.stage import Stage


class TestStage(Stage):
    def __init__(self, start_x: int):
        obstacles = [
            Pipe({'x': 0, 'y': 500})
        ]
        super().__init__(start_x, width=500, obstacles=obstacles)
