from ursina import *


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/skybox.png'),
            scale=150,
            double_sided=True)
