import zmq
import json

def listening_server(port, tcp, udp):
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
		talker.send_string('hello')
		print json.loads(msg)

def main():
	listening_server(5505, True, False)

if __name__ == '__main__':
	main()


