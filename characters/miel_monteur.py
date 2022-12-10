import pygame
from characters.character import Character


class MielMonteur(Character):
    def __init__(self, position):
        sprites = {
            'default': [
                pygame.image.load('sprites/miel_monteur/mielmonteur-idle-2-00.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-idle-2-01.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-idle-2-02.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-idle-2-03.png'),
            ],
            'running':[
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-00.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-01.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-02.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-03.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-04.png'),
                pygame.image.load('sprites/miel_monteur/mielmonteur-run-05.png'),
            ]
        }
        super().__init__(bounding_box={'height': 200, 'width': 200}, sprites=sprites, rotation_speed=5, animation_cooldown=20, position=position)


