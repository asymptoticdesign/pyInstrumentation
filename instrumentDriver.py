"""
Title: instrumentDriver
Description: A multi-purpose instrumentation driver for controlling lab equipment with python
Date Started: 24 Jan 2012
Last Modified: 5 Feb 2012
http://asymptoticdesign.wordpress.com/
This work is licensed under a Creative Commons 3.0 License.
(Attribution - NonCommerical - ShareAlike)
http://creativecommons.org/licenses/by-nc-sa/3.0/

In summary, you are free to copy, distribute, edit, and remix the work.
Under the conditions that you attribute the work to the author, it is for
noncommercial purposes, and if you build upon this work or otherwise alter
it, you may only distribute the resulting work under this license.

Of course, these permissions may be waived with permission from the author.
"""

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
