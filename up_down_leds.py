
import board
import neopixel
import time
import random

number_leds = 100 # update number of leds
board_pin = board.D18 # update board pin
pixels = neopixel.NeoPixel(board.D18, number_leds, brightness=0.5, auto_write=False, pixel_order=neopixel.RGB)

def randomColor():
    return [random.randrange(256), random.randrange(256), random.randrange(256)]

def main():
    slow = 0.02 # update speed
    highValuePosition = 0
    goUp = True
    generalColor = randomColor()

    while True:
        time.sleep(slow)

        # apply color only for valid pixels
        for i in range(number_leds):
            color = [0,0,0]
            if highValuePosition > i:
                color = generalColor
            pixels[i] = color
        
        # change directions
        if highValuePosition == number_leds:
            goUp = False
        elif highValuePosition == 0:
            generalColor = randomColor()
            goUp = True
        
        if goUp:
            highValuePosition += 1
        else:
            highValuePosition -= 1
        
        pixels.show()

main()