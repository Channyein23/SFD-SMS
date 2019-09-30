import serial
import RPi.GPIO as GPIO
import os, time
import serial
import handler

class SMS(handler.AbstractHandler):
    def __init__(self):
        self.port = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)
    
    def handle(self, request):
        if request['threat'] > 15:
            self.sendSMS(str(request))
        super().handle(request)
        
    def sendSMS(self, message):
        self.port.write('AT\r\n'.encode('utf-8'))
        rcv = self.port.read(10)
        time.sleep(1)

        self.port.write('ATE0\r\n'.encode('utf-8'))
        rcv = self.port.read(10)
        time.sleep(1)

        self.port.write('AT+CMGF=1\r\n'.encode('utf-8'))
        rcv = self.port.read(10)
        time.sleep(1)

        self.port.write('AT+CNMI=2,1,0,0,0\r\n'.encode('utf-8'))
        rcv = self.port.read(10)
        time.sleep(1)

        self.port.write('AT+CMGS="+959425624447"\r\n'.encode('utf-8'))
        rcv = self.port.read(10)
        time.sleep(1)

        self.port.write((message + '\r\n').encode('utf-8'))
        rcv = self.port.read(10)

        self.port.write("\x1A".encode('utf-8'))
        for i in range(10):
            rcv = self.port.read(10)
            print (rcv)

if __name__ == '__main__':
	sender = SMS()
	sender.sendSMS('Hello')
