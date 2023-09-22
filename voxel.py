from ursina import *


class Voxel(Button):
    def __init__(self, position: object = (0, 0, 0), texture: object = texture) -> object:
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            texture=texture,
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=.5,
            collider='box')

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=self.texture)
            # if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
            # if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
            # if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)

            if key == 'right mouse down':
                # punch_sound.play()
                destroy(self)
