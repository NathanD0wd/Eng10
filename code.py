true = True
false = False

import math
import time
from adafruit_circuitplayground import cp

exec(open('punchobjects.py').read())
exec(open('pragma.py').read())
exec(open('sinmult.py').read())
exec(open('input.py').read())
exec(open('drawing.py').read())

def instance_create(x, y, obj, color=(20,20,20)):
    chump = obj()
    g.gameobjects.append(chump)
    chump.x = x
    chump.y = y
    chump.color = color

def main():
    print("- init complete -")
    while (true):
        g.count += 1
        if not cp.switch:
            j=0
            while j<10:
                cp.pixels[j] = (0, 0, 10+sinmult(g.count+j*20, 5, 10))
                j += 1
            time.sleep(g.updatespeed)
            continue
        i = 0
        input()
        draw_full((0, 0, 0))
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].step()
            i += 1
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].draw()
            i += 1
        i = 0
        led_update()
        time.sleep(g.updatespeed)

    print("you managed to break out of main, asshole")


main()
