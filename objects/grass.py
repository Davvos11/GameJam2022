import pygame
from objects.object import Object


class Grass(Object):
    def __init__(self, position=None, width=100):
        sprites = {
            'default':
                [pygame.image.load('sprites/blocks/GrassBlock.png')]
        }
        super().__init__({"width": width, "height": 100}, sprites=sprites, position=position, )
