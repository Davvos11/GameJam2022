from typing import Dict

from objects.object import Object


class Pipe(Object):
    def __init__(self, position=None):
        # TODO: Pipe sprites
        super().__init__({"width": 50, "height": 200}, {}, position=position)
