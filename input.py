class input:
    hit = 0
    held = 0
    drop = 0

g.left = input()
g.right = input()

def input():

    if cp.button_a:
        if g.right.held >= 1:
            g.right.hit = 0
        else:
            print("righted")
            g.right.hit = 1
        g.right.held += 1
    elif g.right.held >= 1:
        g.right.held = 0
        g.right.drop = 1
        g.right.hit = 0
    else:
        g.right.held = 0
        g.right.drop = 0
        g.right.hit = 0

    if cp.button_b:
        if g.left.held >= 1:
            g.left.hit = 0
        else:
            print("lefted")
            g.left.hit = 1
        g.left.held += 1
    elif g.left.held >= 1:
        g.left.held = 0
        g.left.drop = 1
        g.left.hit = 0
    else:
        g.left.held = 0
        g.left.drop = 0
        g.left.hit = 0
