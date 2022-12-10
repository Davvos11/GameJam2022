from typing import Dict

from objects.object import Object


class Character(Object):
    JUMP_FRAMES = 50
    JUMP_MAX = 2
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """
    def __init__(self, bounding_box: Dict, sprites: Dict, position=None, health=100):
        super().__init__(bounding_box, sprites, position, has_gravity=True)
        self.health = health
        self.last_jump_frame = -(Character.JUMP_FRAMES*Character.JUMP_MAX)
        self._start_y = self.rectangle.y

    def jump(self):
        # You may jump if you are on the ground and stable in the y direction
        if not(self.delta[1] == Object.GRAVITY and self.colliding['y']):
            return

        self.move_up(200, Character.JUMP_FRAMES)

