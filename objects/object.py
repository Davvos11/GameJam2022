from typing import Dict

import pygame


class Object:
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """
    def __init__(self, bounding_box: Dict, sprites: Dict, position=None):
        if position is None:
            position = {'x': 0, 'y': 0}

        self.width = bounding_box['width']
        self.height = bounding_box['height']
        self.sprites = sprites
        self.x = position['x']
        self.y = position['y']

        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

    def _move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
