from typing import List

from objects.question_mark import QuestionMark
from objects.brick import Brick
from stages.stage import Stage


class BrickStage(Stage):
    def __init__(self, start_x: int):
        obstacles = [
            Brick({'x': 100, 'y': 200}),
            QuestionMark({'x': 200, 'y': 200}),
            Brick({'x': 300, 'y': 200}),
            # Grass({'x': 100, 'y': 500})
        ]
        super().__init__(start_x, width=400, obstacles=obstacles)
