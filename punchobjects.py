class gameobject:
    count = 0
    iterations = 0
    color = (10, 10, 10)
    x = -1
    y = -1
    brightness = 1
    def step(me):
        return
    def draw(me):
        brightmult = abs(me.y%1-.5)
        r = me.color[0]*me.brightness*brightmult
        g = me.color[1]*me.brightness*brightmult
        b = me.color[2]*me.brightness*brightmult
        draw_led(round(me.x), round(me.y), (r, g, b))
    def destroy(me):
        g.gameobjects.remove(me)

class manager(gameobject): #general manager that never gets destroyed. starts the measurement process
    def step(me):
        if g.left.hit and not g.measuring:
            print("taking measurments")
            g.measuring = true
            instance_create(-1, -1, screenclearer)
            instance_create(-1, -1, measurer)
            
class screenclearer(gameobject): #that little particle effect after you press the button
    def draw(me):
        me.count += 1
        if me.count < 10:
            draw_full((10-me.count, 10-me.count, 10-me.count))
        else:
            me.destroy()

class measurer(gameobject): #the thing that does the math
    has_run = false
    has_completed = false
    max_speed = 0
    time_to_max = 0
    def step(me):
        x, y, z = cp.acceleration
        speed = (abs(x)+abs(y)+abs(z)-9.8)*g.updatespeed #speed in m/s over 0.025 measurespeed
        print(speed)
        if speed > 1 and not me.has_run:
            me.has_run = true
            me.max_speed = speed
            me.time_to_max = 1
        if me.has_run:
            if me.count < 15:
                me.count += 1
                print(speed)
                if speed > me.max_speed:
                    me.max_speed = speed
                    me.time_to_max = me.count+1
            else:
                me.has_completed = true
        if me.has_completed:
            accel = me.max_speed/(me.time_to_max*g.updatespeed)#calculate acceleration to max speed 
            me.max_speed *= 2.23694#convert max speed to mph
            print("Max Speed: " + str(me.max_speed) + " mph")
            print("Acceleration to Max Speed: " + str(accel) + " m/s^2")
            g.measuring = false
            g.max_speed = me.max_speed
            g.accel = accel
            instance_create(0, 0, counter)
            me.destroy()

class counter(gameobject): #the thing that displays your stats
    detractor1 = -1
    detractor2 = -1
    tickspeed = .3
    def step(me):
        if me.detractor1 == -1:
            me.detractor1 = math.ceil(g.max_speed)
        if me.detractor2 == -1:
            me.detractor2 = math.ceil(g.accel/10)
        
        if me.detractor1 > 0:
            me.detractor1 -= me.tickspeed
        else:
            me.detractor1 = 0
        
        if me.detractor2 > 0:
            me.detractor2 -= me.tickspeed
        else:
            me.detractor2 = 0
        if g.left.hit:
            me.destroy()
    def draw(me):
        
        bincount = math.floor(g.max_speed-me.detractor1)
        leftover = (g.max_speed-me.detractor1)%1
        doneone = false
        i=0
        while i<5: #right side has max speed
            dabool = 1 if (bincount & 2**i) else 0
            if dabool:
                draw_led(1, 4-i, (10, 10-leftover*10, 10-leftover*10))
                leftover = 0
            i += 1
        #bincount = math.floor(g.max_speed%1*10)
        bincount = math.floor(g.accel/10-me.detractor2)
        leftover = (g.accel/10-me.detractor2)%1
        doneone = false
        i=0
        while i<5: #left side has acceleration
            dabool = 1 if (bincount & 2**i) else 0
            if dabool:
                draw_led(0, 4-i, (10, 10-leftover*10, 10-leftover*10))
                leftover = 0
            i += 1