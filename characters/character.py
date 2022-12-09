from typing import Dict


from objects.object import Object


class Character(Object):
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """
    def __init__(self, bounding_box: Dict, sprites: Dict, position=None, health=100):
        super().__init__(bounding_box, sprites, position, gravity=True)
        self.health = health
