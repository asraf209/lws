#This is a test application that connects to the sensor board
#and reads from any sensors that are changing

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
#from request_handler import put_value_change
#from register_module import register_phidget
import json

#Triggered/run in the event that a sensor value has hanged. 
#e.value returns the value of the current sensor in whatever
#units the sensor is being measured in. For example, the
#slider is measured from 1-1000. The light sensor is measured
#from 0-100%. The index is the integer value index of the port
#that the sensor is plugged in at. With our board it ranges from 0-5. 
def sensorChanged(e):
 print ("Sensor change at %i: %i" % (e.index, e.value))
 #put_value_change(e.value,e.index,'1234')
 

#Create and connect to the device using the InterfaceKit() method.
#This method depends on the device that we are using. For us, it
#happens to be the interfacekit.
try:
  print 'creating the interface kit'
  device = InterfaceKit()
except RuntimeError as e:
  print("Error when trying to create the device: %s" % e.message)

#This connects to the device.
try:
  print 'connecting to the device!'
  device.openPhidget()
except PhidgetException as e:
  print ("Exception when trying to connect %i: %s" % (e.code, e.detail))		
  exit(1)

device.setOnSensorChangeHandler(sensorChanged)


#Only here to block until user keyboard input, which will end the program.
character = str(raw_input())

#we have to close the phidget after we are done..
device.closePhidget()
