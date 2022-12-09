from typing import Dict

from objects.object import Object


class AirPlane(Object):
    def __init__(self, position=None):
        # TODO: Pipe sprites
        super().__init__({"width": 200, "height": 50}, {}, position=position)
