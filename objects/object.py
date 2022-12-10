from typing import Dict

import pygame


class Object:
    # TODO: Borders with debug mode
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """

    def __init__(self, bounding_box: Dict, sprites: Dict, position=None, gravity=False):
        if position is None:
            position = {'x': 0, 'y': 0}

        self.width = bounding_box['width']
        self.height = bounding_box['height']
        self.sprites = sprites
        self._position = position
        self.gravity = gravity
        self.speed = {'x': 0, 'y': 0}

        self.rectangle = pygame.Rect(self._position['x'], self._position['y'], self.width, self.height)

    def _move_instant(self, delta_x=0, delta_y=0):
        self.rectangle.move_ip(delta_x, delta_y)
        self._position['x'] += delta_x
        self._position['y'] += delta_y

    def _check_collisions(self, other_objects):
        rectangles = [object.rectangle for object in other_objects]
        rectangles.remove(self.rectangle)
        return self.rectangle.collidelist(rectangles)

    def update_position(self, other_objects: ['Object']):
        # Add gravity
        if self.gravity:
            self.speed['y'] += 0.01

        # Try to apply movement based on speed (first x then y)
        for direction in ['x', 'y']:
            # Update the rectangle position
            self._position[direction] += self.speed[direction]
            self.rectangle.x = self._position['x']
            self.rectangle.y = self._position['y']

            collision = self._check_collisions(other_objects)
            if collision < 0:
                continue

            # Set the new position next to / above / below the object it collides with
            object = other_objects[collision]
            if self.speed[direction] > 0:
                self._position[direction] = object._position[direction] - (self.width if direction == 'x' else self.height)
            else:
                self._position[direction] = object._position[direction]

            self.rectangle.x = self._position['x']
            self.rectangle.y = self._position['y']
            # Set the speed in this direction to 0
            self.speed[direction] = 0

    def move_right_instant(self, delta_x):
        assert delta_x > 0
        self._move_instant(delta_x=delta_x)

    def move_left_instant(self, delta_x):
        assert delta_x < 0
        self._move_instant(delta_x=-delta_x)

    def move_up_instant(self, delta_y):
        assert delta_y < 0
        self._move_instant(delta_y=-delta_y)

    def move_down_instant(self, delta_y):
        assert delta_y > 0
        self._move_instant(delta_y=delta_y)

