#Miscelenous client backend functions
from uuid import getnode as get_mac
import hashlib

#generates the a device_id value
#In order to generate a random value I am taking the MAC address of the device, then hashing it using
#MD5 and return the first 
def gen_id_val():
	id_val = hashlib.md5(str(get_mac())).hexdigest()
	return id_val

#gets the local IP address of the client- has to be done is some conviluded way
#only works in unix kernals 2.5 and 2.6
def get_local_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
	
	
