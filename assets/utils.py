from PIL import Image

up = Image.open('stone_block1.png')
east = Image.open('stone_block2.png')
north = Image.open('stone_block3.png')
west = Image.open('stone_block4.png')
south = Image.open('stone_block5.png')
down = Image.open('stone_block6.png')


def generate():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            image = Image.new("RGBA", up.size)
                            image.paste(up, (0, 0), up) if a == 1 else 0
                            image.paste(east, (0, 0), east) if b == 1 else 0
                            image.paste(north, (0, 0), north) if c == 1 else 0
                            image.paste(west, (0, 0), west) if d == 1 else 0
                            image.paste(south, (0, 0), south) if e == 1 else 0
                            image.paste(down, (0, 0), down) if f == 1 else 0
                            image.save(f"stone_block/{a}{b}{c}{d}{e}{f}.png")


generate()
