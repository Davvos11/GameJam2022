from typing import Dict

import pygame


class Object:
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

    def _move(self, delta_x=0, delta_y=0):
        self.rectangle.move_ip(delta_x, delta_y)
        self._position['x'] += delta_x
        self._position['y'] += delta_y

    def update_position(self, other_objects: ['Object']):
        # Add gravity
        if self.gravity:
            self.speed['y'] += 0.01

        # Try to apply movement based on speed (first x then y)
        for d in ['x', 'y']:
            # Update the rectangle position
            self._position[d] += self.speed[d]
            self.rectangle.x = self._position['x']
            self.rectangle.y = self._position['y']

            # Check for collision
            rectangles = [obj.rectangle for obj in other_objects]
            rectangles.remove(self.rectangle)
            collision = self.rectangle.collidelist(rectangles)
            if collision > -1:
                # Set the new position next to / above / below the object it collides with
                obj: 'Object' = other_objects[collision]
                self._position[d] = obj._position[d] - (self.width if d == 'x' else self.height)\
                    if self.speed[d] > 0 else obj._position[d]
                self.rectangle.x = self._position['x']
                self.rectangle.y = self._position['y']
                # Set the speed in this direction to 0
                self.speed[d] = 0

    def move_right(self, delta_x):
        assert delta_x > 0
        self._move(delta_x=delta_x)

    def move_left(self, delta_x):
        assert delta_x < 0
        self._move(delta_x=-delta_x)

    def move_up(self, delta_y):
        assert delta_y < 0
        self._move(delta_y=-delta_y)

    def move_down(self, delta_y):
        assert delta_y > 0
        self._move(delta_y=delta_y)