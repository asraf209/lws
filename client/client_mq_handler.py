import zmq
import json
def client_mq(port,upd,tcp):
	context = zmq.Context()
	
	talker = context.socket(zmq.REQ)
	talker.connect('tcp://localhost:%s'%port)
	
	talker.send('Hallooo')
	msg = talker.recv()
	print msg

def send_json(json_to_send,port,udp,tcp):
        context = zmq.Context()

        talker = context.socket(zmq.REQ)
        talker.connect('tcp://lws.at-band-camp.net:%s'%port)

        talker.send_json(json_to_send)
        msg = talker.recv()
        return msg


def main():
	#client_mq(5505,True,False)
	test_dict = {'hi':'this is a test','datur':1234}
	send_json(json.dumps(test_dict),5505,True,False)

if __name__ == '__main__':
	main()
	
