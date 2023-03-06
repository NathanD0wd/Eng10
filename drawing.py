def draw_led(x, y, color):
    if y > 4 or x > 1 or y < 0 or x < 0:
        return false
    if x == 1:
        g.pixelstates[4-y] = color
    else:
        g.pixelstates[5+y] = color
    return true
def draw_led_pos(pos, color):
    if pos > 9 or pos < 0:
        return false
    else:
        g.pixelstates[pos] = color
        return true
def draw_full(color):
    i=0
    while i < 10:
        g.pixelstates[i] = color
        i += 1
def led_update():
    i=0
    while i < 10:
        cp.pixels[i] = g.pixelstates[i]
        i += 1