#import time
from time import sleep
from adafruit_circuitplayground import cp

print("hello <your name>")
while true:
  cp.red_led = true
  sleep(0.5)
  cp.red_led = false
  sleep(0.5)
