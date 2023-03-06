true = True
false = False

exec(open('gameobjects.py').read())
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

import math
import time
from adafruit_circuitplayground import cp


max_speed = 0
time_to_max = 0
accel = 0
num_twos_accel = 0
num_decimal_speed = 0
has_run = false
display = 1
check = false

def main():
    while (true):
        if not cp.switch:
            time.sleep(0.05)
            continue
        i = 0
        input()
        while i < 10:
            g.pixelstates[i] = (0, 0, 0)
            i += 1
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].step()
            i += 1
        i = 0
        while i < len(g.gameobjects):
            g.gameobjects[i].draw()
            i += 1
        i = 0
        while i < 10:
            cp.pixels[i] = g.pixelstates[i]
            i += 1
        time.sleep(g.updatespeed)


main()
