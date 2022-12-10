import pygame
from pygame import *
import numpy

from characters.miel_monteur import MielMonteur
from objects.object import Object
from stages.test_stage import TestStage
from stages.test_stage2 import TestStage2

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
    current_animation = 'default'

    #TODO randomly generate stages
    stages = [
        TestStage(start_x=1000),
        TestStage2(start_x=1500)
    ]

    for stage in stages:
        objects.extend(stage.obstacles)

    STEP_SIZE = 1.5

    # Main loop
    running = True
    while running:
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            break
        if keys[K_RIGHT]:
            MIEL.move_right(STEP_SIZE)
        if keys[K_LEFT]:
            MIEL.move_right(STEP_SIZE)

        for event in pygame.event.get():
            # Quit on ESCAPE or close
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed()[pygame.K_UP]:
                MIEL.jump()

        # Draw background
        screen.fill(COLOURS['gray'])
        # Draw characters
        for obj in objects:
            obj.apply_moves(objects)

            # Probably temporary, but draw sprites if provided, else draw blue rectangle
            if obj.sprites:
                sprite = obj.sprites[current_animation][obj.animation_count]
                sprite = pygame.transform.scale(sprite, (obj.width, obj.height))
                screen.blit(sprite, (obj.rectangle.x, obj.rectangle.y))
                obj.animation_count = (obj.animation_count + 1) % len(obj.sprites[current_animation])
            else:
                pygame.draw.rect(screen, COLOURS['blue'], obj.rectangle)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
