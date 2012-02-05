"""
Title: readSerial
Description: Read serial data from arduino microcontroller
Date Started: 17 Jan 2012
Last Modified: 4 Feb 2012
http://asymptoticdesign.wordpress.com/
This work is licensed under a Creative Commons 3.0 License.
(Attribution - NonCommerical - ShareAlike)
http://creativecommons.org/licenses/by-nc-sa/3.0/

In summary, you are free to copy, distribute, edit, and remix the work.
Under the conditions that you attribute the work to the author, it is for
noncommercial purposes, and if you build upon this work or otherwise alter
it, you may only distribute the resulting work under this license.

Of course, these permissions may be waived with permission from the author.

Usage:
scottnla@faraday-cage:~/$ python readSerial.py [filename w/o extension]
"""

import sys
import serial
import getpass
import datetime
import instrumentDriver

"""location of the arduino"""
location = '/dev/ttyACM0'

"""Connect to the arduino"""
arduino = instrumentDriver.serialDevice(location)

"""Successfully connected!"""
filename = str(sys.argv[1])
logFile = open(filename+'.log','w')
dataFile = open(filename+'.dat','w')

"""The main loop -- data is taken here and written to file"""
while True:
	try:
		"""retrieve the raw analog number from the arduino's ADC"""
		datum = arduino.read()
		"""process it to a meaningful number:"""
		print datum
		dataFile.write(datum)
	except:
		"""this allows for the user to CTRL-C out of the loop, and closes/saves the file we're writing to."""
		dataFile.close()
		break

"""Rip out relevant information and write to log file"""
logFile.write('User: '+getpass.getuser()+'\n')
logFile.write('Date: '+datetime.datetime.now().strftime("%Y-%m-%d")+'\n')
logFile.write('Time: '+datetime.datetime.now().strftime("%H:%M:%S")+'\n')
logFile.write('Experimental Parameters:\n')
sample = raw_input('Sample used: ')
logFile.write('Sample: '+sample+'\n')
notes = raw_input('Notes: ')
logFile.write('Notes: '+notes+'\n')
