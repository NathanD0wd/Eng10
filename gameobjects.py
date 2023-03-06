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

class menu(gameobject):
    x = -1
    y = 0
    def step(farting):
        if g.right.hit:
            instance_create(0, 4, note, (10, 10, 10))


class note(gameobject):
    x = 0
    y = 5
    def step(me):
        me.y -= .1
        if me.y < 0:
            instance_create(me.x, 0, redpart, (10, 0, 0))
            me.destroy()
        elif me.y < .5 and g.left.hit:
            print("he he lol")
            instance_create(me.x, 0, redpart, (0, 0, 10))
            me.destroy()

class redpart(gameobject):
    def step(me):
        me.brightness -= .1
        if me.brightness <= 0:
            me.destroy()


class tone:
    def __init__(me, val, time):
        me.val = val
        me.time = time

class song(gameobject):
    notes = [
        tone(932, 1.0),
        tone(622, 1.2),
        tone(1244, 1.4),
        tone(1046, 1.6),
        tone(932, 1.8),
        tone(622, 2.0),
        tone(932, 2.2),
        tone(830, 2.4),
        tone(783, 2.6),
        tone(783, 2.8),
        tone(622, 3.0),
        tone(932, 3.2),
        tone(1244, 3.4),
        tone(1396, 3.6),
        tone(1567, 3.8),
    ]
    def step(me):
        me.count += 1.0
        i = 0
        #print("hey")
        if len(me.notes) <= 0:
            return
        #print(me.count, me.notes[0].time*60)
        while i<len(me.notes):
            break #delete for pwnage
            if me.count >= me.notes[i].time*60+.2*60:
                cp.stop_tone()
                me.notes.remove(me.notes[i])
            if len(me.notes) <= 0:
                break
            if me.count >= me.notes[i].time*60:
                print(me.notes[i].val)
                cp.start_tone(me.notes[i].val)
            i += 1

class tempdude(gameobject):
    x = 1
    y = 4
    brightness = .2
    amount = 64
    def step(me):
        dude = cp.temperature-27.5
        print(dude, cp.temperature)
        me.color = (255-dude*me.amount, 0, dude*me.amount)
        print(dude*me.amount)

class speeddude(gameobject):
    x = -1
    y = -1
    brightness = .2
    amount = 2
    defaults = (0, 0, 9.8)
    pos = [0, 0, 0]
    def step(me):
        if cp.switch:
            me.defaults = cp.acceleration   
            me.pos = [0, 0, 0]
            print("risetto")
        x, y, z = cp.acceleration
        x -= me.defaults[0]
        y -= me.defaults[1]
        z -= me.defaults[2]
        me.pos[0] += x
        me.pos[1] += y
        me.pos[2] += z
        draw_led(1, 2, (-x*me.amount, 0, x*me.amount))
        draw_led(1, 3, (-y*me.amount, 0, y*me.amount))
        draw_led(1, 4, (-z*me.amount, 0, z*me.amount))
        #print(x)
        #print(y)
        #print(z)
        #print(me.pos[0])
        #print(me.pos[1])
        #print(me.pos[2])

class manager(gameobject):
    def step(me):
        if g.left.hit and not g.measuring:
            print("taking measurments")
            g.measuring = true
            instance_create(0, 0, screenclearer)
            instance_create(0, 0, measurer)
    def draw(me):
        return
            
class screenclearer(gameobject):
    def draw(me):
        me.count += 1
        if me.count < 10:
            draw_full((10-me.count, 10-me.count, 10-me.count))
        else:
            me.destroy()

class measurer(gameobject):
    has_run = false
    def step(me):
        x, y, z = cp.acceleration
        speed = (abs(x)+abs(y)+abs(z)-9.8)*g.updatespeed #speed in m/s over 0.025 measurespeed
        print(speed)
        if speed > 1:
            me.has_run = true
            max_speed = speed
            for i in range(15):
                x, y, z = cp.acceleration
                speed = (abs(x)+abs(y)+abs(z)-9.8)*0.025
                print(speed)
                if speed > max_speed:
                    max_speed = speed
                    time_to_max = i+1
                time.sleep(g.updatespeed)
        if me.has_run:
            accel = max_speed/(time_to_max*g.updatespeed)#calculate acceleration to max speed 
            max_speed *= 2.23694#convert max speed to mph
            print("Max Speed: ", end ="")
            print(max_speed, end="" )
            print(" mph")
            print("Acceleration to Max Speed: ", end ="")
            print(accel, end="" )
            print(" m/s^2")
            g.measuring = false
            me.destroy()
    def draw(me):
        return
class counter(gameobject):
    def step(me):
        while (display != -1):
            time.sleep(1.5)
            display = 1
            
            max_speed = max_speed - 1
            print(max_speed)
            green = 1
            blue = 0
            red = 0
            for x in range(max_speed):
                num = x / 5
                if num >= 1:
                    if num < 2:
                        red = 1
                if num >= 2:
                    if num < 3:
                        green = 0
                if num >= 3:
                    if num < 4:
                        red = 0
                        blue = 1
                if num >= 4:
                    red = 1
                cp.pixels[x%5] = ( 50 * red , 50 * green , 50 * blue)
                time.sleep(0.3)
            
            time.sleep(0.7)
            num_decimal_speed = ((max_speed % 1) / 0.1) - 0.5
            print(num_decimal_speed)
            green = 1
            blue = 0
            red = 0
            for x in range(num_decimal_speed):
                num = x / 5
                if num >= 1:
                    green = 0
                    blue = 1
                cp.pixels[x%5+5] = ( 50 * red , 50 * green , 50 * blue)
                time.sleep(0.3)
            
            while (display == 1):
                time.sleep(0.25)
                if cp.button_a:
                    display = 0
                    cp.pixels.fill((0,0,0))
                if cp.button_b:
                    display = -1
                if cp.switch == false:
                    display = -1
            time.sleep(0.7)
            if ( display == -1 ):
                cp.pixels.fill((0,0,0))
                break
            
            num_twos_accel = accel / 2
            green = 1
            blue = 0
            red = 0
            for x in range(num_twos_accel):
                num = x / 10
                if num >= 1:
                    if num < 2:
                        red = 1
                if num >= 2:
                    if num < 3:
                        green = 0
                if num >= 3:
                    if num < 4:
                        red = 0
                        blue = 1
                if num >= 4:
                    red = 1
                cp.pixels[x%10] = ( 50 * red , 50 * green , 50 * blue)
                time.sleep(0.3)

            while (display == 0):
                time.sleep(0.25)
                if cp.button_a:
                    display = 1
                    cp.pixels.fill((0,0,0))
                if cp.button_b:
                    display = -1
                if cp.switch == false:
                    display = -1
            cp.pixels.fill((0,0,0))
    def draw(me):
        return