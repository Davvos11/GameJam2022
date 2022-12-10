from typing import Dict

import pygame


class Object:
    GRAVITY = 0.5
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

    def apply_gravity(self, other_objects: ['Object']):
        if not self.gravity:
            return

        # Temporarily move the box and see if there are collisions
        self._position['y'] += Object.GRAVITY
        self.rectangle.y = self._position['y']

        # Check for collisions
        collision = self._check_collisions(other_objects)
        if collision < 0:
            # Return can be seen as a commit for the change
            return

        # If there are collisions, bound to top of the box
        collision_object = other_objects[collision]
        self._position['y'] = collision_object.rectangle.top - self.height

    def move_right_instant(self, delta_x):
        assert delta_x > 0
        self._move_instant(delta_x=delta_x)

    def move_left_instant(self, delta_x):
        assert delta_x > 0
        self._move_instant(delta_x=-delta_x)

    def move_up_instant(self, delta_y):
        assert delta_y > 0
        self._move_instant(delta_y=-delta_y)

    def move_down_instant(self, delta_y):
        assert delta_y > 0
        self._move_instant(delta_y=delta_y)

