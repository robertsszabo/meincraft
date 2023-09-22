from ursina import *


class Player(Entity):

    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk
        # up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt