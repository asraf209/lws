#Connecting and interacting with the database

from pymongo import Connection
from bson.json_util import dumps as mongo_dumps
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
def post_value_change(temp_change):
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
	
	#check to see if the device id exsits
	if collection.find({"devid":dev_reg['devid']}).count() == 0:
		return False
	else:
		return True

#checks the IP address of the device to see if it is current, if it isn't then we update it
def check_current_ip(dev_reg):
	connection = Connection()
	db = connection.lws
	collection = db.devices
	collection.update({"devid":dev_reg['devid']},{"$set":{"ipaddress":dev_reg['ipaddress']}})
	
#registeres the device base on the JSON structure that is passed to the function
def register_device(dev_reg):
	connection = Connection()
	db = connection.lws
	collection = db.devices
	collection.insert(dev_reg)

#lists all of the devices that have been registered. Resturns them as a collection of JSON
#objects and the processing/formatting can be done on the front end
def list_all_devices():
	all_devices = []
	connection = Connection()
	db = connection.lws
	collection = db.devices
	devices = collection.find()
	for device in devices:
		temp_dict = json.loads(mongo_dumps(device))
		for k in temp_dict.keys():
			if k == '_id':
				del temp_dict[k]
		all_devices.append(temp_dict)
	return all_devices

#dumps data based on parameters passed to the function. Will return a JSON structure with values matching this. 
def dump_value_data(dev_id):
	connection = Connection()
	db = connection.lws
	collection = db.tempData
	data = collection.find()
	all_data = []
	for point in data:
		data_dict = json.loads(mongo_dumps(point))
		for k in data_dict.keys():
			if k == '_id':
				del data_dict[k]
		all_data.append(data_dict)
	return all_data
		#return mongo_dumps(data)

#gets the last 24 hours about a specific device and the information for that device as well.
def get_device_info(dev_id):
	dev_dict = {}
	connection = Connection()
	db = connection.lws
	collection = db.devices
	dev_data = collection.find({'devid':dev_id})
	dev_only_dict = json.loads(mongo_dumps(dev_data))
		
	#getting this months worth of data
	connection = Connection()
	db = connection.lws
	collection = db.tempData
	this_year = datetime.now().year
	this_month = datetime.now().month
	month_data = json.loads(mongo_dumps(collection.find({"phid":dev_id,"year":this_year,"m":this_month})))
	
	dev_dict['dev_info']=dev_only_dict
	print dev_only_dict
	dev_dict['month_info']=month_data
	print month_data

	return dev_dict
	

#updates the database with a few aspects about a device:
#name- what you name the device
#location - where the device is, not sure how we want to take this into the database
def update_device(dev_id,data_dict):
	return 0


def run():
	data = get_device_info('1b7239de')
	
	for key in data:
		moar_datur = key
		for moar in moar_datur:
			print 'Key: %s value: %s'%(moar,moar_datur[key])

#	print dump_all_data()
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
       

if __name__ == '__main__':
        run()

