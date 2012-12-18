#Fake client that simulates readings to the aggregation layer
import time
import random
from threading import Thread
import md5
import hashlib
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

def gen_fake_ip(list):
	root_add='192.168.1.'
	mach_id=random.randrange(200)+100
	if mach_id < 252:
		root_add='192.168.1.%s'%mach_id
	else:
	 	root_add = gen_fake_ip(list)
	
	for key in list:
		if list[key] == root_add:
			root_add = gen_fake_ip(list)	
		
	return root_add 

#generates a fake ID value
def gen_fake_id_val():
	id_val = hashlib.md5(str(random.random())).hexdigest()
	return id_val[:8]



if __name__ == '__main__':
	#run()
	#reg_test_ip_vals= ['192.168.1.101', '192.168.1.204', '192.168.1.202', '192.168.1.107', '192.168.103', '192.168.1.106']					
	#for ip in reg_test_ip_vals:
		#time.sleep(4)
		#register_device(ip,gen_id_val())
	
	fake_dev_map={}	
	counter = 0
	
	while True and counter < 150:
		time.sleep(1)
		fake_id = gen_fake_id_val()
		fake_dev_map[fake_id] = ' '
		fake_ip = gen_fake_ip(fake_dev_map)
		fake_dev_map[fake_id]=fake_ip
		#print '%s has the ip of %s'%(fake_id,fake_ip)				
		register_device(fake_ip,fake_id)
		
	#reg_test()






