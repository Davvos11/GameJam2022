from typing import Dict
import functools

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
        self._downforce = Object.GRAVITY
        self.speed = {'x': 0, 'y': 0}
        self.rectangle = pygame.Rect(self._position['x'], self._position['y'], self.width, self.height)
        self.moves=[]

    def _add_move(self, delta_x=0, delta_y=0, frames=1):
        self.moves.append(Move(delta_x, delta_y, frames))

    def _move_rect(self, delta, direction):
        self._position[direction] += delta
        if direction == 'x':
            self.rectangle.x = self._position[direction]
        elif direction == 'y':
            self.rectangle.y = self._position[direction]

    def _check_collisions(self, other_objects):
        rectangles = [object.rectangle for object in other_objects]
        rectangles.remove(self.rectangle)
        return self.rectangle.collidelist(rectangles)

    def apply_moves(self, other_objects: ['Object']):
        # Each move creates an x and y delta, combine them and apply the moves
        move_deltas = [move.get_frame_delta() for move in self.moves]

        # Append gravity as move
        if self.gravity:
            move_deltas.append((0, Object.GRAVITY))

        if len(move_deltas) == 0:
            return

        # Get the net move
        delta = functools.reduce(
            lambda accumulator, deltas: (accumulator[0] + deltas[0], accumulator[1] + deltas[1]),
            move_deltas
        )

        # For both directions check whether the move can be made:
        for index, direction in enumerate(['x', 'y']):
            # Temporarily move the box and see if there are collissions
            self._move_rect(delta[index], direction)

            # Check for collisions
            collision = self._check_collisions(other_objects)
            if collision < 0:
                # continue can be seen as a commit for the change
                continue

            # If there are collisions, place back to old coord
            self._move_rect(-delta[index], direction)

    def move_right(self, delta_x, frames=1):
        assert delta_x > 0
        self._add_move(delta_x=delta_x, frames=frames)

    def move_left(self, delta_x, frames=1):
        assert delta_x > 0
        self._add_move(delta_x=-delta_x, frames=frames)

    def move_up(self, delta_y, frames=1):
        assert delta_y > 0
        self._add_move(delta_y=-delta_y, frames=frames)

    def move_down(self, delta_y, frames=1):
        assert delta_y > 0
        self._add_move(delta_y=delta_y, frames=frames)


class Move:
    def __init__(self, delta_x, delta_y, frames):
        self.stepY = delta_y // frames
        self.stepX = delta_x // frames
        self.frames = frames

    def get_frame_delta(self):
        if self.frames == 0:
            del self
            return 0, 0
        self.frames -= 1
        return self.stepX, self.stepY
