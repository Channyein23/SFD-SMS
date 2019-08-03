import fuzzy
import flame
import dht11
import sms

if __name__ == '__main__':
    dht = dht11.DHT11(pin = 4)
    fis = fuzzy.FIS.instance()
    dht.set_next(fis)
    dht.handle({})