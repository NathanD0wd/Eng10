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

def instance_create(x, y, obj, color=(20,20,20)): #use to create a gameobject
    chump = obj()
    g.gameobjects.append(chump)
    chump.x = x
    chump.y = y
    chump.color = color

def main():
    print("- init complete -")
    while (true):
        g.count += 1
        if not cp.switch: #if off play the animation and dont do update logic
            j=0
            while j<10:
                cp.pixels[j] = (0, 0, 5+sinmult(g.count+j*20, 5, 5))
                j += 1
            time.sleep(g.updatespeed)
            continue
        i = 0
        input()
        draw_full((0, 0, 1)) #refresh screen. i'm doing it with a tiny bit of blue
        i = 0
        while i < len(g.gameobjects): #perform gameobject step event
            g.gameobjects[i].step()
            i += 1
        i = 0
        while i < len(g.gameobjects): #perform gameobject draw event. there is no difference in processing, its mostly just for readability
            g.gameobjects[i].draw()
            i += 1
        i = 0
        led_update()
        time.sleep(g.updatespeed)

    print("you managed to break out of main, asshole")


main()
