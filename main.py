from map import Map
from ursina import *

from player import Player
from first_person_controller import FirstPersonController
from sky import Sky

app = Ursina()

if __name__ == '__main__':

    window.vsync = True
    window.size = window.fullscreen_size
    window.exit_button.visible = False
    window.fps_counter.enabled = True

    Sky()
    Map()
    for z in range(-8, 8):
        for x in range(-8, 8):
            Map.update(x, 0, z, random.randint(1, 4))

    player = Player(model='cube', origin_y=0, color=color.orange)
    wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
    wall_right = duplicate(wall_left, x=4)
    fpc = FirstPersonController(y=2, origin_y=-.5)

    app.run()
