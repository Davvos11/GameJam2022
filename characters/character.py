from typing import Dict


class Character:
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """
    def __init__(self, bounding_box: Dict, sprites: Dict, position=None, health=100):
        if position is None:
            position = {'x': 0, 'y': 0}

        self.width = bounding_box['width']
        self.height = bounding_box['height']
        self.sprites = sprites
        self.x = position['x']
        self.y = position['y']
        self.health = health

    def _move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
