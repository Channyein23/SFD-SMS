import serial
import RPi.GPIO as GPIO
import OS, time
import serial
          
      
           ser = serial.Serial(
              
               port='/dev/ttyAMA0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
           counter=0
          
      
           while 1:
               ser.write('AT\n')
               time.sleep(1)
 
              x=ser.readline()
               print x # you should 