import os
import serial

"""Function to looks for connected USB instruments"""
def list_instruments():
       inst_list = []
       return inst_list

class serialDevice:
       def __init__(self,location):
              self.device = location
              self.port = serial.Serial(location,9600)

       def write(self,command):
              self.port.write(command)
              
       def read(self):
              return self.port.readline()

class usbDevice:
       """Initializes a connection to the device port [presumably usb]"""
       def __init__(self, location):
              self.device = location
              self.connect = os.open(location, os.O_RDWR)
           
       def write(self, command):
              os.write(self.connect, command);
            
       def read(self, length = 4000):
              return os.read(self.connect, length)
            
       def getID(self):
              self.write("*IDN?")
              return self.read(100)
        
class instrument:
       """Initialize instrument given a port, e.g. /dev/usbtmc0/"""
       def __init__(self, location, conType):
           if conType.lower() == 'serial':
                  self.port = serialDevice(location)

           if conType.lower() == 'usb':
                  self.port = usbDevice(location)
                  self.id = self.port.getID()
                  print self.id
           else:
                  print "Device type not recognized"

       def write(self, command):
           self.port.write(command)
           
       def read(self, command):
           return self.port.read(command)
