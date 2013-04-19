import zmq
import json
import threading
from db_interface import device_checkin,post_value_change

class ThreadedServer(threading.Thread):
	def run(self):
		start_listening_server(5505,True,False)
	def start_listening_server(port, tcp, udp):

        	#create the context
       		context = zmq.Context()

        	#create the socket
        	talker = context.socket(zmq.REP)
        	if tcp:
                	talker.bind('tcp://*:%s'%port)
        	if udp:
                	talker.bind('udp://*:%s'%port)
        	while True:
                	msg = talker.recv()
                	#recive_dict = json.loads(msg)

                	device_checkin(msg)
                	post_value_change(msg)
                	talker.send('_data_put')
			

def start_listening_server(port, tcp, udp):
	
	#create the context
	context = zmq.Context()
	
	#create the socket
	talker = context.socket(zmq.REP)	
	if tcp:
		talker.bind('tcp://*:%s'%port)
	if udp:
		talker.bind('udp://*:%s'%port)
	count = 0
	while True:
		msg = talker.recv()
		#recive_dict = json.loads(msg)
		
		#device_checkin(msg)
		#print json.loads(msg)
		return_val = device_checkin(json.loads(msg))
		post_value_change(json.loads(msg))
		#talker.send('okay')
		#print msg
		if return_val == 0:
			talker.send('_data_put')
		else:
			talker.send(return_val)
		count +=1
		print count
		#context.term()
		#start_listening_server(5505, True, False)
		
def main():
	start_listening_server(5505, True, False)
	#t= ThreadedServer()
	#t.start()

if __name__ == '__main__':
	main()
	


