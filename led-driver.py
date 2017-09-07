# Main file to drive LEDs

import time
import math
from dotstar import Adafruit_DotStar

num_pixels = 288 # Number of LEDs in strip

strip = Adafruit_DotStar(num_pixels, 12000000, order='bgr') # Initialize strip
strip.begin()
strip.setBrightness(10) # Save my eyes

# Rainbow Display
def moving_rainbow(frequency, start = 0):
    for i in range(0, num_pixels):
        color = get_rainbow_color(frequency, i, start)
        strip.setPixelColor(i, color[0], color[1], color[2])

def get_rainbow_color(frequency, start, offset = 0):
    # Uses three out of sync sin waves to have a smooth transition between colors
    # Frequency is how quickly it moves throught the rainbow
    # Start is position in rainbow
    # Offset is how much the rainbow is offset by (duh)
    red   = int(math.sin(frequency * (start + offset)) * 127 + 128)
    green = int(math.sin(frequency * (start + offset) + 2 * math.pi / 3) * 127 + 128)
    blue  = int(math.sin(frequency * (start + offset) + 4 * math.pi / 3) * 127 + 128)
    return [red, green, blue]

# Sets all pixels on strip to same color
def set_all_pixels(r, g, b):
    for i in range(0, num_pixels):
        strip.setPixelColor(i, r, g, b)

start = 0.0
while True:
    strip.show()
    #color = get_rainbow_color(0.1, start)
    #set_all_pixels(color[0], color[1], color[2]) Solid rainbow effect
    moving_rainbow(0.1, start)
    start += 1 # Shifts rainbow down strip
    time.sleep(1.0 / 60) # Pause 20 milliseconds (~50 fps)
