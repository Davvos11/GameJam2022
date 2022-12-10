import pygame
from objects.object import Object


class QuestionMark(Object):
    def __init__(self, position=None):
        sprites = {
            'default':
                [pygame.image.load('sprites/blocks/QuestionMarkBlock.png')]
        }
        super().__init__({"width": 100, "height": 100}, sprites=sprites, position=position, )
