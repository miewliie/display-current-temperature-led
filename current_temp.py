from lib.pixels import Color, Pixels

DELAY = 0.25
color = (255, 0, 0)


if __name__ == '__main__':
    x, y = [5, 7]
    pixels: Pixels = Pixels()
    pixels.set(x, y, Color(*color))
    pixels.show()

