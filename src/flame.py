
import RPi.GPIO as GPIO
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def register_callback(callback):
    GPIO.add_event_detect(channel, GPIO.FALLING, callback = lambda channel: callback())
    
if __name__ == '__main__':
	def callback():
		print("Flame!")
	register_callback(callback)
	while True:
		time.sleep(10)
