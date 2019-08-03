import RPi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


instance = dht11.DHT11(pin=4)

while True:
	result = instance.read()
	if result.is_valid():
		print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

	time.sleep(1)
