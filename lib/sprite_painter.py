from lib.pixels import *
from typing import NamedTuple


class MonochromeSprite(NamedTuple):

    width: int
    """Width of the sprite"""

    height: int
    """Height of the sprite"""

    pixels: list[tuple[int, int]]
    """The list of pixels representing the sprite"""


def draw_pixels(
    pixels: Pixels,
    position: tuple[int, int],
    pixel_list: list[tuple[int, int]],
    color: Color
    ):
    """ Start at position x, y and draw sprite with given list of
    x, y coordinate with color provide"""
    
    for pixel in pixel_list:
        x, y = pixel
        pos_x, pos_y = position
        x = pos_x + x
        y = pos_y + y

        pixels.set(x, y, color)


def draw_monochrome_sprite(
    pixels: Pixels,
    sprite: MonochromeSprite,
    position: tuple[int, int],
    color: Color
):
    """ Draw a sprite with one color """

    draw_pixels(pixels, position, sprite.pixels, color)
