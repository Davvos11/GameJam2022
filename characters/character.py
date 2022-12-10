from typing import Dict

from objects.object import Object


class Character(Object):
    JUMP_FRAMES = 50
    """
    :param bounding_box, width and height of model
    :param sprites, set of sprites for the model
    """
    def __init__(self, bounding_box: Dict, sprites: Dict, rotation_speed=0, animation_cooldown=10, position=None, health=100):
        super().__init__(bounding_box=bounding_box, sprites=sprites, rotation_speed=rotation_speed, position=position, has_gravity=True)
        self.health = health
        self._start_y = self.rectangle.y
        self.animation_cooldown_max = animation_cooldown
        self.animation_cooldown_current = animation_cooldown

    def jump(self):
        # You may jump if you are on the ground and stable in the y direction
        if not(self.delta[1] == Object.GRAVITY and self.colliding['y']):
            return

        self.move_up(200, Character.JUMP_FRAMES)

    def move_miel_right(self, delta_x, other_obstacles: ['Object'], frames=1, type=0):
        for obstacle in other_obstacles:
            obstacle.move_left(delta_x, frames=frames, type=type)

    def move_miel_left(self, delta_x, other_obstacles, frames=1, type=0):
        for obstacle in other_obstacles:
            obstacle.move_right(delta_x, frames=frames, type=type)

    def animate(self):
        if self.animation_cooldown_current == 0:
            self.animation_count = (self.animation_count + 1) % len(self.sprites[self.current_animation])
        self.animation_cooldown_current = (self.animation_cooldown_current + self.animation_cooldown_max - 1) % self.animation_cooldown_max
        if self.animation_count >= len(self.sprites[self.current_animation]):
            self.animation_count = 0
