#!/usr/bin/env python3
### BEGIN INIT INFO
# Provides:          thermo_fan.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start Thermo Fan Process at boot time
# Description:       Checks CPU at regular intervals and switches fan on/off
### END INIT INFO

# Based on Tutorial by Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
# https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

pin = 18 # The pin ID, edit here to change it
checkInterval = 5 # Check the Temp every x seconds

tempTrigger = 60 # The temp in Celsius when to switch the fan on
tempDetrigger = tempTrigger - 5 # The temp in Celsius when to switch the fan off

fanStatusOn = 0 # Fan Status - 1 = On, 0 = Off

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print("Temp - {0}".format(temp)) #Uncomment here for testing
    return temp

def checkTempForFan():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp > tempTrigger and fanStatusOn == 0:
        #print("Switching Fan ON")
        return setFan(1)
    if CPU_temp <= tempDetrigger and fanStatusOn == 1:
        #print("Switching Fan OFF")
        return setFan(0)
    print("{},{}".format(CPU_temp,fanStatusOn))
    return -1

def setFan(setFanOn):
    global pin
    global fanStatusOn
    if fanStatusOn != setFanOn:
        GPIO.output(pin, setFanOn)
    return setFanOn

try:
    setup()
    print("Temp,Fan")
    while True:
        checkTempForFan()
        sleep(checkInterval) # Delay before next check
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program
