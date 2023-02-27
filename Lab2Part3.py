import board
import pwmio
from adafruit_circuitplayground import cp
import adafruit_motor.servo
from time import sleep
# Setup Section
pwm = pwmio.PWMOut(board.A1, frequency=50)
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2600)
# Function Section
def light_to_servo_pos(light):
  light_max = 320
  return 180 - ((light/light_max) * 180) #Delete '180 -' to switch angle
# Loop Section
while True:
  servo.angle = light_to_servo_pos(cp.light)
  print(servo.angle)
  sleep(0.5)
