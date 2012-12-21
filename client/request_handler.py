#A hanlder for putting data to the aggregator node
import urllib2
import httplib
import requests
from datetime import datetime
import time as time
import json
import socket

agg_add='http://127.0.0.1:5000/'

#puts a temperature change onto the server
def put_value_change(value, phidget_id, sensor_id):
	headers = {'content-type':'application/json'}
	temp_data = {
			 'd':datetime.now().day,
			 'y':datetime.now().year,
			 'month':datetime.now().month, 
		         'h':datetime.now().hour,
		         'min':datetime.now().minute,
		         's':datetime.now().second,
			 #'ms':int(round(time_.time()*1000)), 
		         'val':value,
		         'phid':phidget_id,
		         'sensid':sensor_id,
		     }

	#old code that is supposedly no good to actually implement
	#if you are behind a proxy
	#opener = urllib2.build_opener(urllib2.HTTPHandler)
	#request = urllib2.Request('http://127.0.0.1/', data=temp_data)
	#request.add_header('Content-Type', 'application/json')
	#request.get_method = lambda: 'PUT'
	#url = opener.open(request)
	#print 'putting the request!'
	temp_data=json.dumps(temp_data)

	the_request = requests.put('%sdevices/updates/value'%agg_add, data=temp_data, headers=headers)
	print the_request.text	


#Function that registeres the device, will return a JSON object if the device has not been registered, 1 if registration
#has been sucessful, 2 if the device has already been registered.
#Data looks like:
#reg_info:

def register_device(ip_address, dev_id):
	#reg_info = {
			#'ipaddress':str(ip_address),
			#'devid':str(dev_id),
			#'d':datetime.now().day,
                        #'y':datetime.now().year,
                        #'month':datetime.now().month,
                        #'h':datetime.now().hour,
                        #'min':datetime.now().minute,
		#}
	reg_info = {
			'min':'hiii',
		}


	headers = {'content-type':'application/json'}
        temp_data = {
                         
			 'ipaddress':ip_address,
			 'devid':dev_id,
			 'd':datetime.now().day,
                         'y':datetime.now().year,
                         'month':datetime.now().month,
                         'h':datetime.now().hour,
                         'min':datetime.now().minute,
                         's':datetime.now().second,
                         #'ms':int(round(time_.time()*1000)), 
                         #'val':'10',
                         #'phid':'123',
                         #'sensid':'0',
                     }

	
	print temp_data
	
	temp_data=json.dumps(temp_data)

        the_request = requests.put('%sdevices/register'%agg_add, data=temp_data, headers=headers)
        print the_request.text
