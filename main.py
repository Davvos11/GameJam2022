import pygame
import numpy

from characters.miel_monteur import MielMonteur
from objects.object import Object
from stages.test_stage import TestStage

COLOURS = {
    'gray': (150, 150, 150),
    'blue': (0, 0, 255)
}


def main():
    # Initialise pygame
    pygame.init()

    # Show window
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    MIEL = MielMonteur({'height': 200, 'width': 50}, {}, {'x': 300, 'y': 500})

    GROUND_HEIGHT = screen.get_height() // 4 * 3
    GROUND = Object({'height': screen.get_height() // 4, 'width': screen.get_width()},
                    {}, {'x': 0, 'y': GROUND_HEIGHT})


    objects = [GROUND, MIEL]

    #TODO randomly generate stages
    stages = [
        TestStage(start_x=1000)
    ]

    for stage in stages:
        objects.extend(stage.obstacles)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            # Quit on ESCAPE or close
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.QUIT:
                running = False

            # Draw background
            screen.fill(COLOURS['gray'])
            # Draw characters
            for obj in objects:
                pygame.draw.rect(screen, COLOURS['blue'], obj.rectangle)

            pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
