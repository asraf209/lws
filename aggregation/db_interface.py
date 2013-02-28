#Connecting and interacting with the database

from pymongo import Connection
from bson.json_util import dumps as mongo_dumps
from datetime import datetime
import json
import time

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
	collection.update({"devid":dev_reg['devid']},{"$set":dev_reg})
	
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
def get_day_dev_info(dev_id):
	dev_data_list = []
	connection = Connection()
	return_dict = {}
	db = connection.lws
	collection = db.devices
	dev_data = collection.find({'devid':dev_id})
	dev_only_dict = json.loads(mongo_dumps(dev_data))	

	#getting this months worth of data
	collection = db.tempData
	this_year = datetime.now().year
	this_month = datetime.now().month
	this_day = datetime.now().day
	print this_day
	month_data = collection.find({"phid":dev_id,"y":this_year,"month":this_month,"d":this_day,"s":0})
	#month_data = collection.find({"phid":"402c8efa","y":this_year,"month":this_month})
	
	for point in month_data:
		data_dict = json.loads(mongo_dumps(point))
		for k in data_dict.keys():
			if k =='_id':
				del data_dict[k]
		#print 'appending: %s'%data_dict
		dev_data_list.append(data_dict)
		
	
	return_dict['dev_info'] = dev_only_dict
	return_dict['data_list'] = dev_data_list

	#print dev_only_dict
	#dev_dict['month_info']=month_data
	#print month_data

	return return_dict
	
#gets the devices current stats
def get_current_stats(dev_id,min_offset):
        dev_data_list = []
        connection = Connection()
        return_dict = {}
  	
	db = connection.lws
        collection = db.devices
        dev_data = collection.find({'devid':dev_id})
	
	for thing in dev_data:
        	dev_only_dict = json.loads(mongo_dumps(thing))

        #getting this months worth of data
       
        db = connection.lws
        collection = db.tempData
        this_year = datetime.now().year
        this_month = datetime.now().month
        this_day = datetime.now().day
        this_hour = datetime.now().hour
	this_minute = datetime.now().minute-min_offset
	this_second = datetime.now().second
       	print this_minute
	current_data = collection.find({"phid":dev_id,"y":this_year,"month":this_month,"d":this_day,"h":this_hour,"min":this_minute}).limit(1)
        #month_data = collection.find({"phid":"402c8efa","y":this_year,"month":this_month})

	for thing in current_data:
		data_dict = mongo_dumps(thing)
		data_dict = json.loads(data_dict)
		#print testa['sensor_data']

	#print current_data.get('sensor_data')
        #data_dict = mongo_dumps(current_data)
	print 'len data dict is %s'%len(data_dict)
        return_dict['dev_info'] = dev_only_dict
        return_dict['data_list'] = data_dict
	
        #print dev_only_dict
        #dev_dict['month_info']=month_data
        #print month_data

	if len(data_dict) == 0:
		print 'len is zero!'
		return get_current_stats(devid,1)
	else:
        	return return_dict



#updates the database with a few aspects about a device:
#name- what you name the device
#location - where the device is, not sure how we want to take this into the database
def update_device(dev_id,data_dict):
	return 0


def run():
	#data = get_day_dev_info('402c8efa')
	data = get_current_stats('402c8efa',0)		
	dev_info = data['dev_info']
	data_list = data['data_list']

	
	print data_list["sensor_data"]


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
	while True:
		time.sleep(1)
		run()

