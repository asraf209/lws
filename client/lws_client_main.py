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
import Queue
import threading
import time
import zmq

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

queue = Queue.Queue()

class threaded_request(threading.Thread):

	def __init__(self,queue,devid):
		threading.Thread.__init__(self)
		self.queue = queue
		self.devid = devid

	def run(self):
		while True:
			sensor_data = self.queue.get()
			print '%s making request: %s'%(self.getName(),sensor_data)
			#ip_addy = get_local_ip('eth0')
			#put_value_change(self.devid,sensor_data,False) 
			json_to_send = json.dumps(sensor_data)
		        context = zmq.Context()

        		talker = context.socket(zmq.REQ)
        		talker.connect('tcp://lws.at-band-camp.net:5505')
		
        		talker.send_json(json_to_send)
        		msg = talker.recv()
        		print msg
        		talker.term()
        		context.term()
			self.queue.task_done()
			print '%s is done!'%self.getName()

def main():
	device = connect_phidget()
	#start = time.time()
	dev_id = gen_id_val()
	#for i in range(0,100000):
		#queue.put(check_sensors(device))
	
	for i in range(0,10):
		#print i
		t = threaded_request(queue,dev_id)
		t.setDaemon(True)
		t.start()
	
	start = time.time()
	for i in range(0,10):
                queue.put(check_sensors(device))

	queue.join()	
	print "Elapsed Time: %s" % (time.time() - start)		


main()

#Only here to block until user keyboard input, which will end the program.
#character = str(raw_input())

#we have to close the phidget after we are done..
#device.closePhidget()
