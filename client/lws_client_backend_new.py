from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from lws_client_backend import gen_id_val, get_local_ip
import time

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

def start_sensors_for_changes():
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

def sensorChanged(e):
 print ("Sensor change at %i: %i" % (e.index, e.value))

def sensor_changes():
	for i in range(8):
		try:
			print 'Sensor %s: value %s'%(i,device.getSensorValue(i))
			
		except:
			print 'Sensor not on the %s port'%i

	#print device.getSensorValue(5)

def run_poller():
	while True:
		time.sleep(2)
		print_sensor_changes()	

if __name__ == '__main__':
	run_poller()
