from typing import Dict
import functools

import pygame


class Object:
    GRAVITY = 1
    # TODO: Borders with debug mode
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """

    def __init__(self, bounding_box: Dict, sprites: Dict, position=None, has_gravity=False):
        self.delta = (0, Object.GRAVITY)
        self.colliding = {
            'x': False,
            'y': False
        }
        if position is None:
            position = {'x': 0, 'y': 0}

        self.width = bounding_box['width']
        self.height = bounding_box['height']
        self.sprites = sprites
        self.has_gravity = has_gravity
        self.rectangle = pygame.Rect(position['x'], position['y'], self.width, self.height)
        self.moves = []
        self.frame = 0

    def _add_move(self, delta_x=0, delta_y=0, frames=1, type=0):
        self.moves.append(Move(delta_x, delta_y, frames=frames, type=type))

    def _move_rect(self, delta, direction):
        if direction == 'x':
            self.rectangle.x += delta
        elif direction == 'y':
            self.rectangle.y += delta

    def _check_collisions(self, other_objects):
        rectangles = [object.rectangle for object in other_objects]
        rectangles.remove(self.rectangle)
        return self.rectangle.collidelist(rectangles)

    def apply_moves(self, other_objects: ['Object']):
        # Each move creates an x and y delta, combine them and apply the moves
        move_deltas = [move.get_frame_delta() for move in self.moves]

        # Append gravity as move
        if self.has_gravity:
            move_deltas.append((0, Object.GRAVITY))

        if len(move_deltas) == 0:
            return

        # Get the net move
        delta = functools.reduce(
            lambda accumulator, deltas: (accumulator[0] + deltas[0], accumulator[1] + deltas[1]),
            move_deltas
        )

        self.delta = delta

        # For both directions check whether the move can be made:
        for index, direction in enumerate(['x', 'y']):
            # Temporarily move the box and see if there are collissions
            self._move_rect(delta[index], direction)

            # Check for collisions
            collision = self._check_collisions(other_objects)
            if collision < 0:
                self.colliding[direction] = False
                # continue can be seen as a commit for the change
                continue
            self.colliding[direction] = True

            # If there are collisions, place back to old coord
            self._move_rect(-delta[index], direction)

        for move in self.moves:
            if move.frames <= 0:
                self.moves.remove(move)

        self.frame += 1

    def move_right(self, delta_x, frames=1, type=0):
        assert delta_x > 0
        self._add_move(delta_x=delta_x, frames=frames, type=type)

    def move_left(self, delta_x, frames=1, type=0):
        assert delta_x > 0
        self._add_move(delta_x=-delta_x, frames=frames, type=type)

    def move_up(self, delta_y, frames=1, type=0):
        assert delta_y > 0
        self._add_move(delta_y=-delta_y, frames=frames, type=type)

    def move_down(self, delta_y, frames=1, type=0):
        assert delta_y > 0
        self._add_move(delta_y=delta_y, frames=frames, type=type)


class Move:
    def __init__(self, delta_x, delta_y, frames, type=0):
        self.stepY = delta_y // frames
        self.stepX = delta_x // frames
        self.frames = frames
        self.type = type

    def get_frame_delta(self):
        if self.frames == 0:
            del self
            return 0, 0
        self.frames -= 1
        return self.stepX, self.stepY
