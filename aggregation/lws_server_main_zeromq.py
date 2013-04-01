import zmq
import json
from db_interface import device_checkin,post_value_change

def start_listening_server(port, tcp, udp):
	SUBSCRIBERS_EXPECTED = 2
	
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
		post_value_change(json.loads(msg))
		talker.send('_data_put')
		
def main():
	start_listening_server(5505, True, False)

if __name__ == '__main__':
	main()


