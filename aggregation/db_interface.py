#Connecting and interacting with the database

from pymongo import Connection
from datetime import datetime
import json

#posts a temperature change to the database at the
#aggregation layer.
#Assumes the following python dictionary/json data sctructure:
#reading:
#	{
#	  'd':date
#	  'h':hour
#	  'm':minute
#	  's':second
#	  'hs':hoursecond
#	  'val':value
#	  'phid':phidgetid
#	  'sensid':sensorid
#	}
def post_temp_change(temp_change):
	connection = Connection()
	#connects us to the lws database
	db = connection.lws
	collection = db.tempData
	collection.insert(temp_change)

#checks to see if the device has been registered based on the JSON structure that
#is passed to the function
def device_registered(dev_reg):
	connection = Connection()
	db = connection.lws
	collection = db.devices
	anything = collection.find(dev_reg)
	if anything is empty:
		return 0
	else:
		return 1	
	

#registeres the device base on the JSON structure that is passed to the function
def register_device(dev_reg):
	connection = Connection()
	db = connection.lws
	collection = db.devices
	devices.insert(dev_reg)


#
#def run():
#	temp_data = {
#        		'd':datetime.now().day,
#			'y':datetime.now().year,
#			'month':datetime.now().month,
#			'h':datetime.now().hour,
#			'min':datetime.now().minute,
#			's':datetime.now().second,
#			'val':88,
#			'phid':129384,
#			'sensid':0,
#       	}
#	
#	post_temp_change(temp_data)
       

#if __name__ == '__main__':
#        run()

