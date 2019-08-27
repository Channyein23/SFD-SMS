import fuzzy
import flame
import dht11
import sms
import time

dht = dht11.DHT11(pin = 4)
fis = fuzzy.FIS.instance()
sender = sms.SMS()

dht.set_next(fis)
fis.set_next(sender)

def onFlame():
    dht.handle({})
    time.sleep(1000)

if __name__ == '__main__':
    flame.register_callback(onFlame)
    while True:
        time.sleep(5000)
