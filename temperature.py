from lib.pixels import *
from lib.sprite_painter import *
from coordinate.num_coordinate import numbers


if __name__ == '__main__':

    pixels: Pixels = Pixels()

    number = '10c'

    for i in range(0, len(number)):

        sprite = MonochromeSprite(height = 8, width = 6, pixels = numbers[number[i]])

        position_x = i * 6 ## the starting point of first sprite at y axis will start at 0,
        ## and the next sprite will start after the previous one.

        position_y = 0 ## the starting point of y axis is always 0 for 32x8 matrix

        draw_monochrome_sprite(pixels, sprite, (position_x, position_y), Color(0, 0, 200))

    pixels.show()
