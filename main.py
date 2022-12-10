import pygame
from pygame import *
import numpy

from characters.miel_monteur import MielMonteur
from objects.object import Object
from stages.test_stage import TestStage
from stages.test_stage2 import TestStage2
from stages.brick_stage import BrickStage
from stages.hill_stage import HillStage

COLOURS = {
    'gray': (150, 150, 150),
    'blue': (0, 0, 255)
}


def main():
    # Initialise pygame
    pygame.init()

    # Show window
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    GROUND_HEIGHT = screen.get_height() // 4 * 3

    MIEL = MielMonteur(position={'x': 300, 'y': GROUND_HEIGHT - 200})
    GROUND = Object({'height': screen.get_height() // 4, 'width': screen.get_width()},
                    {'default': [pygame.image.load('sprites/blocks/GrassBlock.png')]},
                    position={'x': 0, 'y': GROUND_HEIGHT})


    objects = [GROUND, MIEL]

    #TODO randomly generate stages
    stages = [
        # TestStage(start_x=1000),
        # TestStage2(start_x=1500),
        BrickStage(start_x=1000),
        HillStage(start_x=500)
    ]

    for stage in stages:
        objects.extend(stage.obstacles)

    STEP_SIZE = 1.5

    # Main loop
    running = True
    while running:
        keys = key.get_pressed()
        # If no key is pressed, make Miel idle
        if not pygame.event.get():
            MIEL.current_animation = 'default'
            MIEL.rotation_speed = 0
        if keys[K_ESCAPE]:
            break
        if keys[K_RIGHT]:
            MIEL.move_right(STEP_SIZE)
            MIEL.current_animation = 'running'
            MIEL.inversed = False
            MIEL.rotation_speed = MIEL.rotation_speed_default
        if keys[K_LEFT]:
            MIEL.move_left(STEP_SIZE)
            MIEL.current_animation = 'running'
            MIEL.inversed = True
            MIEL.rotation_speed = MIEL.rotation_speed_default
        if keys[K_UP]:
            MIEL.jump()

        for event in pygame.event.get():
            # Quit on ESCAPE or close
            if event.type == pygame.QUIT:
                running = False
            # if pygame.key.get_pressed()[pygame.K_UP]:
            #     MIEL.jump()

        # Draw background
        screen.fill(COLOURS['gray'])
        # Draw characters
        for obj in objects:
            obj.apply_moves(objects)

            # Probably temporary, but draw sprites if provided, else draw blue rectangle
            if obj.sprites:
                obj.animate()
                sprite = obj.sprites[str(obj.current_animation)][obj.animation_count]
                sprite.convert()
                sprite = pygame.transform.scale(sprite, (obj.width, obj.height))
                obj.rotation = (obj.rotation - obj.rotation_speed) % 360
                sprite = rot_center(sprite, obj.rotation)

                if obj.inversed:
                    sprite = pygame.transform.flip(sprite, True, False)
                screen.blit(sprite, (obj.rectangle.x, obj.rectangle.y))
            else:
                pygame.draw.rect(screen, COLOURS['blue'], obj.rectangle)

        pygame.display.update()

    pygame.quit()


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

if __name__ == '__main__':
    main()
