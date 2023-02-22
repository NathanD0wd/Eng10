import board
import pwmio
from adafruit_circuitplayground import cp
from adafruit_hcsr04 import HCSR04
import adafruit_motor.servo
from time import sleep
# Setup Section

pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section
def servo_pos(dist):
    dist_min = 5
    dist_max = 50
    dist = min((max((dist, dist_min)), dist_max))
    return (((dist-dist_min)/(dist_max-dist_min)) * 180)

led_brightness = 0.25
t = 0
dt = 0.25
sonar = HCSR04(trigger_pin=board.TX, echo_pin=board.A6)
cp.pixels.fill((255,0,255))
cp.pixels.brightness = 0

# Function Section
def pixel_flip():
    if cp.pixels.brightness > 0:
        cp.pixels.brightness = 0
    else:
        cp.pixels.brightness = led_brightness

while True:
    try:
        d = sonar.distance
        servo.angle = servo_pos(d)
        print((d, servo.angle))
# Closer than 15 cm is Dangerously Close
        if d <=5:
            pixel_flip()
            if t >= 1.0:
                cp.play_tone(440, 0.25)
                t = 0
# Closer than 15 cm is Very Close
        elif d <= 15:
            pixel_flip()
# Closer than 30 cm is Close
        elif d <= 30:
            if t >= 1.0:
                pixel_flip()
                t = 0
# Farther than 25 cm is Safe
        else:
            cp.pixels.brightness = 0
        print((d,))
        t+=dt
    except RuntimeError:
        print("Retrying!")
    sleep(dt)
