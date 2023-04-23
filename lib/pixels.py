import math
from rpi_ws281x import PixelStrip as Adafruit_NeoPixel, Color


# LED strip configuration:
LED_PIN        = 18        # GPIO pin connected to the pixels (must support PWM!).
LED_DMA        = 5         # DMA channel to use for generating signal (try 5)
MATRIX_HEIGHT  = 8
MATRIX_WIDTH   = 32
LED_COUNT      = MATRIX_HEIGHT * MATRIX_WIDTH # Number of LED pixels.

class Pixels:
    """A beautiful matrix of pixels."""

    _neopixels: Adafruit_NeoPixel
    """The stripe of LEDs correspoding to the matrix. Internal use only."""

    def __init__(self, brightness = 30):
        """Set brightness to 0 for darkest and 255 for brightest."""

        self._neopixels = Adafruit_NeoPixel(
              num = LED_COUNT,
              pin = LED_PIN,
              dma = LED_DMA,
              brightness = brightness
        )
        self._neopixels.begin()

    def __enter__(self):
        self.clear()
        self.show()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.clear()
        self.show()

    def show(self):
        """Flushes all uncommited pixel changes to the pixels."""

        self._neopixels.show()

    def fill(self, color: Color):
        """Completely fills the matrix with the given color."""

        for i in range(LED_COUNT):
          self._neopixels.setPixelColor(i, color)

    def clear(self):
        """Sets the matrix into a clean state."""

        self.fill(color = Color(0, 0, 0))

    def set(self, x: int , y: int, color: Color):
        """Set the pixel at the given coordinates with the given color."""

        if x < 0 or x >= MATRIX_WIDTH:
            return

        if y < 0 or y >= MATRIX_HEIGHT:
            return

        led_number: int = x * MATRIX_HEIGHT + y
        if (math.floor(led_number / MATRIX_HEIGHT) % 2) == 1:
          self._neopixels.setPixelColor((x + 1) * MATRIX_HEIGHT - y - 1, color)
        else:
          self._neopixels.setPixelColor(led_number, color)
