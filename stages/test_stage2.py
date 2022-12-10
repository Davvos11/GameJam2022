from objects.airplane import AirPlane
from stages.stage import Stage


class TestStage2(Stage):
    def __init__(self, start_x: int, ground_y):
        obstacles = [
            AirPlane({'x': 0, 'y': 200})
        ]
        super().__init__(start_x, width=100, obstacles=obstacles, ground_y=ground_y)
