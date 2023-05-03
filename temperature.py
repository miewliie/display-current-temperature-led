from lib.pixels import *
from lib.sprite_painter import *
from coordinate.num_coordinate import numbers
from coordinate.glyph_coordinate import weather


def draw_temp(pixels, temp_celsius):
    """ Draw temperature, degree symbol, and minus sign if necessary. """
    
    temp_celsius = temp_celsius + 'c'

    for i in range(0, len(temp_celsius)):
        sprite = MonochromeSprite(height = 8, width = 6, pixels = numbers[temp_celsius[i]])
        
        ## The first sprite starting point of the x-axis is 0. The next sprite 
        ## will be positioned after the previous one.
        position_x = i * 6

        ## The starting point of the y-axis is always 0 for a 32x8 matrix.
        position_y = 0 

        draw_monochrome_sprite(pixels, sprite, (position_x, position_y), Color(0, 0, 200))


def draw_wcondition(pixels, w_condition):
    """ Draw colorful weather condition glyph. """

    ## You can check the API documentation for a list of weather conditions. 
    ## If you are using OpenWeather like me, you should have the same list as shown below.
    etc_glyph_set = {'Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Ash', 'Squall'}

    w_condition = 'Etc' if w_condition in etc_glyph_set else w_condition

    sprite = ColorfulSprite(
        height=8,
        width=12,
        layers=weather[w_condition]
    )

    ## For the glyphs of weather conditions, I set starting location of the x-axis at position 20.
    ## The initial color will be overridden at the 'draw_colorful_sprite' method. 
    position_x = 20
    position_y = 0
    draw_colorful_sprite(pixels, sprite, (position_x, position_y), Color(255, 0, 0))


if __name__ == '__main__':

    pixels: Pixels = Pixels()

    ## Later, we will obtain this data from an API.
    temp_celsius, weather_condition = ['-8', 'Snow']

    draw_temp(pixels, temp_celsius)
    draw_wcondition(pixels, weather_condition)

    pixels.show()
