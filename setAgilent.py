#!/usr/bin/python
import numpy
import matplotlib.pyplot as plot
import time
import instrumentDriver
import scipy
 
""" Example program to plot the Y-T data from Channel 1"""
 
# Initialize our scope
test = instrumentDriver.instrument("/dev/usbtmc0")
 
# Stop data acquisition
#test.write("APPL:SIN 5.0E+3, 3.0, 0")
freqs = scipy.linspace(1.0e5,1.0e6,10)
test.write("OUTP ON")

for freq in freqs:
    test.write("APPL:SIN "+str(freq)+",5.0")
    time.sleep(2)

test.write("OUTP OFF")
"""
# Grab the data from channel 1
test.write(":WAV:POIN:MODE NOR")
 
test.write(":WAV:DATA? CHAN1")
rawdata = test.read(9000)
data = numpy.frombuffer(rawdata, 'B')
 
# Get the voltage scale
test.write(":CHAN1:SCAL?")
voltscale = float(test.read(20))
 
# And the voltage offset
test.write(":CHAN1:OFFS?")
voltoffset = float(test.read(20))
 
# Walk through the data, and map it to actual voltages
# First invert the data (ya rly)
data = data * -1 + 255
 
# Now, we know from experimentation that the scope display range is actually
# 30-229.  So shift by 130 - the voltage offset in counts, then scale to
# get the actual voltage.
data = (data - 130.0 - voltoffset/voltscale*25) / 25 * voltscale
 
# Get the timescale
test.write(":TIM:SCAL?")
timescale = float(test.read(20))
 
# Get the timescale offset
test.write(":TIM:OFFS?")
timeoffset = float(test.read(20))
 
# Now, generate a time axis.  The scope display range is 0-600, with 300 being
# time zero.
time = numpy.arange(-300.0/50*timescale, 300.0/50*timescale, timescale/50.0)
 
# If we generated too many points due to overflow, crop the length of time.
if (time.size > data.size):
    time = time[0:600:1]
 
# See if we should use a different time axis
if (time[599] < 1e-3):
    time = time * 1e6
    tUnit = "uS"
elif (time[599] < 1):
    time = time * 1e3
    tUnit = "mS"
else:
    tUnit = "S"
 
# Start data acquisition again, and put the scope back in local mode
test.write(":RUN")
test.write(":KEY:FORC")
 
# Plot the data
plot.plot(time, data)
plot.title("Oscilloscope Channel 1")
plot.ylabel("Voltage (V)")
plot.xlabel("Time (" + tUnit + ")")
plot.xlim(time[0], time[599])
plot.show()
"""
