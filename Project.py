import time
from adafruit_circuitplayground import cp

max_speed = 0
time_to_max = 0
accel = 0
num_twos_accel = 0
num_decimal_speed = 0
has_run = False
display = 1
check = False

while (True):
    while (cp.switch):
        if cp.button_b:
            has_run = False
            display = 1
            cp.pixels.fill((0,50,0))
            time.sleep(0.2)
            cp.pixels.fill((0,0,0))
            time.sleep(1.5)
            cp.pixels.fill((50,50,50))
            time.sleep(0.2)
            cp.pixels.fill((0,0,0))
            while (has_run == False):
                x, y, z = cp.acceleration
                speed = (abs(x)+abs(y)+abs(z)-9.8)*0.025#speed in m/s over 0.025 seconds
                print(speed)
                if speed > 1:
                    has_run = True
                    max_speed = speed
                    for i in range(15):
                        x, y, z = cp.acceleration
                        speed = (abs(x)+abs(y)+abs(z)-9.8)*0.025
                        print(speed)
                        if speed > max_speed:
                            max_speed = speed
                            time_to_max = i+1
                        time.sleep(0.025)
                time.sleep(0.025)
            accel = max_speed/(time_to_max*0.025)#calculate acceleration to max speed 
            max_speed *= 2.23694#convert max speed to mph
            print("Max Speed: ", end ="")
            print(max_speed, end="" )
            print(" mph")
            print("Acceleration to Max Speed: ", end ="")
            print(accel, end="" )
            print(" m/s^2")
            #For output
            while (display != -1):
                time.sleep(1.5)
                num_twos_accel = accel / 2
                green = 1
                blue = 0
                red = 0
                display = 1
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
                while (display == 1):
                    time.sleep(0.25)
                    if cp.button_a:
                        display = 0
                        cp.pixels.fill((0,0,0))
                    if cp.button_b:
                        display = -1
                    if cp.switch == False:
                        display = -1
                time.sleep(0.7)
                if ( display == -1 ):
                    cp.pixels.fill((0,0,0))
                    break

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

                while (display == 0):
                    time.sleep(0.25)
                    if cp.button_a:
                        display = 1
                        cp.pixels.fill((0,0,0))
                    if cp.button_b:
                        display = -1
                    if cp.switch == False:
                        display = -1
                cp.pixels.fill((0,0,0))
        time.sleep(0.05)
    time.sleep(0.5)
