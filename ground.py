from ursina import *
from voxel import Voxel


class Ground(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            texture=load_texture('assets/stone_plate.png'),
            scale=150,
            double_sided=True)

    # def numbers_to_strings(argument):
    #     switcher = {
    #         1: 'assets/grass_block.png',
    #         2: 'assets/stone_plate.png',
    #         3: 'assets/brick_block.png',
    #         4: 'assets/dirt_block.png'
    #     }
    #     return switcher.get(argument, "nothing")



