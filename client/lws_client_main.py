#This is a test application that connects to the sensor board
#and reads from any sensors that are changing

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from request_handler import put_value_change, register_device
from lws_client_backend import gen_id_val,get_local_ip
from request_handler import put_value_change
#from register_module import register_phidget
import json
from time import sleep
from logging_framework import *

#Create and connect to the device using the InterfaceKit() method.
#This method depends on the device that we are using. For us, it
#happens to be the interfacekit.

def connect_phidget():
	try:
  		log_info('creating the interface kit')
  		device = InterfaceKit()
	except RuntimeError as e:
  		log_error("Error when trying to create the device: %s" % e.message)

	#This connects to the device.
	try:
 		#print 'connecting to the device!'
  		device.openPhidget()
	except PhidgetException as e:
 		log_warning("Exception when trying to connect %i: %s" % (e.code, e.detail))		
  		exit(1)

	return device

#polls all of the sensors that are available/plugged in and retruns a dict with
#the sensor index plus the value. There has to be a way to query the phidget
#I/0 board to see which sensors are attached. Takes the constructed device as
#an arugement
def check_sensors(device):
	#since we can have up to 8 sensors, we check to all 8 ports
	values_dict={}
	for n in range(0,8):
		try:
			#print 'checking sensor on %s'%n
			values_dict[n] = device.getSensorValue(n)
		except:
			#print 'no sensor attached to port %s'%n
			values_dict[n] = 'N/A'

	return values_dict

if __name__ == '__main__':
	#get the id_val of the device
	dev_id = gen_id_val()
	device = connect_phidget()
	#We can use a timer thread for this.. just wanted to keep it simple for
	#my own sake.
	while True:
		sleep(3)
		device.setOutputState(0,0)
		#getting the IP here, don't really need to do this after some recent updates
		ip_addy = get_local_ip('eth0')
		log_info('IP is: %s'%ip_addy)		
		register_device(ip_addy,dev_id)
		sensor_data = check_sensors(device)
		log_info(sensor_data)
		response = put_value_change(dev_id,sensor_data,True)
		if response == 0:
			device.setOutputState(0,1)
	device.closePhidget()


#Only here to block until user keyboard input, which will end the program.
#character = str(raw_input())

#we have to close the phidget after we are done..
#device.closePhidget()
