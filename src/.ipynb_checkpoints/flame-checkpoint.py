import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

def register_callback(callback):
    GPIO.add_event_callback(channel, lambda channel: callback())
    
if __name__ = '__main__':
    time.sleep(1000)