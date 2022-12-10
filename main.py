import pygame
from pygame import *
import numpy
from random import shuffle

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

DEBUG_COLOURS = [
    (255, 0, 0), # RED
    (0, 255, 0), # GREEN
    (255, 105, 180) # PINK
]

DEBUG = False
stages = [
    BrickStage,
    HillStage,
    TestStage,
    TestStage2
]


def generate_stages(previous_cycle, ground_height, start_x):
    if previous_cycle:
        while previous_cycle[0] is stages[-1]:
            shuffle(stages)

    result = []
    for stage in stages:
        result.append(stage(start_x, ground_height))
        start_x += stage.width
    return result


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

    level_stages = generate_stages(None, GROUND_HEIGHT, 500)

    obstacles = []

    debug_colour_index = 0
    stage_debug_rects = []

    for stage in level_stages:
        obstacles.extend(stage.obstacles)
        stage_debug_rects.append(get_stage_debug_rect(stage, debug_colour_index, screen.get_height()))
        debug_colour_index = (debug_colour_index + 1) % len(DEBUG_COLOURS)

    objects.extend(obstacles)

    object_debug_rects = []
    for obj in objects:
        object_debug_rects.append(get_object_debug_rect(obj, debug_colour_index))
        debug_colour_index = (debug_colour_index + 1) % len(DEBUG_COLOURS)

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
            MIEL.move_miel_right(STEP_SIZE, other_obstacles=obstacles)
            MIEL.current_animation = 'running'
            MIEL.inversed = False
            MIEL.rotation_speed = MIEL.rotation_speed_default
        if keys[K_LEFT]:
            MIEL.move_miel_left(STEP_SIZE, other_obstacles=obstacles)
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

        if DEBUG:
            # for i in range(len(stage_debug_rects)):
            #     screen.blit(stage_debug_rects[i], (stages[i]., 0))

            for i in range(len(object_debug_rects)):
                screen.blit(object_debug_rects[i], (objects[i].rectangle.x, objects[i].rectangle.y))

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


def get_stage_debug_rect(stage, debug_colour_index, screen_height):
    debug_colour = DEBUG_COLOURS[debug_colour_index]
    debug_rect = pygame.Surface((stage.width, screen_height))
    debug_rect.set_alpha(50)
    debug_rect.fill(debug_colour)
    return debug_rect


def get_object_debug_rect(obj, debug_colour_index):
    debug_colour = DEBUG_COLOURS[debug_colour_index]
    debug_rect = pygame.Surface((obj.width, obj.height))
    debug_rect.set_alpha(50)
    debug_rect.fill(debug_colour)
    return debug_rect


if __name__ == '__main__':
    main()
