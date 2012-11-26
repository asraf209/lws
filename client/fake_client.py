#Fake client that simulates readings to the aggregation layer
import time
import random
from threading import Thread
import md5
from request_handler import put_value_change, register_device
from lws_client_backend import gen_id_val, get_local_ip

#inteval in seconds for the fake client to attempt to post something
#the aggreation later
interval = 2 
#the number of clients to simulate
client_number = 10
#the temperature sensor_id ( for now, at least)
sensor_id = 0

#returns a temperature value between 0-100
def random_temp():
	return random.randrange(100)+1	

#returns a random phidget ID. Some testing going on
#here in terms of efficiency of hashing functions to
#create a randon sensor id
def random_phidget_id():
	phidget_id = str(random.randrange(1000)+1)
	return  phidget_id

class fake_client(Thread):
	def run(self):
		phidget_id = random_phidget_id()
		while True:
			#print 'putting a temp change!'
			global sensor_id
			put_value_change(random_temp(),phidget_id,sensor_id)
			time.sleep(interval)
	
	def random_phidget_id():
        	phidget_id = md5.new(str(random.randrange(1000)+1)).digest()
        	return  phidget_id[5:]

	def random_temp():       
		return random.randrange(100)+1

def run():
	global client_number
	for number in xrange(client_number):
		fake_client().start()

#test the registration of the device
def reg_test():
	register_device(get_local_ip('eth0'), gen_id_val())

if __name__ == '__main__':
	#run()					
	reg_test()






