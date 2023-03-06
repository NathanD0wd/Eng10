class g: #global object that contains all kinds of fun things
    merry = "christmas"

g.pixelstates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g.count = 0
g.measuring = false
g.updatespeed = .025
g.max_speed = 0
g.accel = 0
print("- loading -")
g.gameobjects = [
    manager()
    #menu(),
    #song(),
    #speeddude(),
]