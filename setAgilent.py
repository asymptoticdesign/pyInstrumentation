"""
Title: setAgilent
Description: set the frequency and power for a sine wave on an Agilent 33210A function generator
Date Started: 28 Jan 2012
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

Usage:
scottnla@faraday-cage:~/$ python setAgilent.py [frequency of sinusoid] [amplitude of sinusoid]
"""

import sys
import time
import instrumentDriver
 
 
"""Initialize our function generator, connected via usb"""
agilent = instrumentDriver.instrument("/dev/usbtmc0",'usb')

"""Turn the output of the function generator on"""
agilent.write("OUTP ON")

"""
Apply a sine wave with given frequency and amplitude; the APPL:SIN text is taken from the Agilent 33210A's manual -- for other equipment, see its user guide for the appropriate strings to send to it
"""
agilent.write("APPL:SIN "+str(sys.argv[1])+','+str(sys.argv[2]))

"""This causes the program to sleep for 5 seconds -- the function generator stays on during this duration."""
time.sleep(5)

"""Turn the output of the function generator off"""
agilent.write("OUTP OFF")
