from PIL import Image
from voxel import Voxel

elements = [[[0 for col in range(-64, 64)] for col in range(5)] for row in range(-64, 64)]


class Map:

    def getvalue(x, y, z):
        return elements[x][y][z]

    def topisrendered(x, y, z):
        return 1 if elements[x][y + 1][z] == 0 else 0

    def botisrendered(x, y, z):
        return 1 if elements[x][y - 1][z] == 0 else 0

    def eastisrendered(x, y, z):
        return 1 if elements[x + 1][y][z] == 0 else 0

    def northisrendered(x, y, z):
        return 1 if elements[x][y][z + 1] == 0 else 0

    def westisrendered(x, y, z):
        return 1 if elements[x - 1][y][z] == 0 else 0

    def southisrendered(x, y, z):
        return 1 if elements[x][y][z - 1] == 0 else 0

    def calculateTexture(x, y, z):
        return f'assets/stone_block/{Map.topisrendered(x, y, z)}{Map.botisrendered(x, y, z)}{Map.eastisrendered(x, y, z)}{Map.northisrendered(x, y, z)}{Map.westisrendered(x, y, z)}{Map.southisrendered(x, y, z)}.png'

    def update(x, y, z, val):
        elements[x][y][z] = val
        Voxel(position=(x, y, z), texture=Map.calculateTexture(x, y, z))
