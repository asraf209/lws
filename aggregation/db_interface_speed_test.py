#Connecting and interacting with the database

from pymongo import Connection
from bson.json_util import dumps as mongo_dumps
from datetime import datetime
import datetime
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
	#print temp_change
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

#posts a device check in to the database
def device_checkin(temp_data_json):
        #print temp_data_json
	
	#print 'Trying to check the device in!'
	connection = Connection()
        db = connection.lws
        try:
		#print 'Connecting to db.deviceCheckIn'
		collection = db.deviceCheckIn
        except:
		return 0
		print 'Cannot create the collection db.deviceCheckIn?'
	
	#print 'Loading into data dictonary'
	try:
		data_dict = json.dumps(temp_data_json)
		data_dict = json.loads(data_dict)	
		print data_dict['sensor_data']
	except:
		return 0
		print 'CANNOT MAKE DICT'        

	#print data_dict['sensor_data']	

	#print 'len of data dict is %s'%len(data_dict)
	for thing in data_dict:
                if thing == 'sensor_data':
			print 'foudn it!'
                        del data_dict[thing]
			break

	try:
		print 'Checking to see if the device is in the checkin'
	       	if collection.find({'phid':data_dict['phid']}).count() == 0:
                	print 'Adding device to checkin!'
			collection.insert(data_dict)
        	else:
			print 'Updating device checkin!'
                	collection.update({"phid":data_dict['phid']},{"$set":data_dict}) 
	except:
		print 'DB ERROR'

#gets the last time a device checked into/interacted with the aggregation node
def get_last_checkin(devid):
	connection = Connection()
        db = connection.lws
        collection = db.deviceCheckIn
	checkin = {}        

	for val in  collection.find({'phid':devid}):
		checkin = json.loads(mongo_dumps(val))
	
	return checkin


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
       	last_checkin = get_last_checkin(dev_id)
        db = connection.lws
        collection = db.tempData
        this_year = last_checkin['y']
        this_month = last_checkin['month']
        this_day = last_checkin['d']
        this_hour = last_checkin['h']
	this_minute = last_checkin['min']
	this_second = last_checkin['s']
       	print this_minute
	current_data = collection.find({"phid":dev_id,"y":this_year,"month":this_month,"d":this_day,"h":this_hour,"min":this_minute}).limit(1)
        #month_data = collection.find({"phid":"402c8efa","y":this_year,"month":this_month})
	
	if current_data.count() == 0:
                print 'len is zero!'
                return get_current_stats(dev_id,1)
        else:
        	for thing in current_data:
			data_dict = mongo_dumps(thing)
			data_dict = json.loads(data_dict)
			#print testa['sensor_data']

        	return_dict['dev_info'] = dev_only_dict
        	return_dict['data_list'] = data_dict

		return return_dict

#updates the database with a few aspects about a device:
#name- what you name the device
#location - where the device is, not sure how we want to take this into the database
def update_device(dev_id,data_dict):
	return 0

def get_data_timespan(dev_id,start_date,end_date,celc):
	#http://lws.at-band-camp.net/devices/device/data/time/json?devid=1234&startdate=12389124&enddate=123124&celc=123123123
	#start_date_dict = parse_date(start_date)
	#end_date_dict = parse_date(end_date)
	#db.tempData.find({phid:'1b7239de',month:{'$gte': ,'$lt': },d:{'$gte':7,'$lt':8},y:{'$gte':,'$lt'},h:{'$gte':,'$lt':},min:{'$gte': ,'$lt': },s:{'$gte': ,'$lt': })
	#get_data_timespan_db(start_date_dict,end_date_dict,dev_id)	

	return 0
def get_data_timespan_db_date_query(dev_id,start_date,end_date,celc):
	return_list=[]
	connection = Connection()
	db = connection.lws
	collection = db.tempData
	#import time
	#start = time.time()
	#db.tempData.find({"h":{$gte:1,$lte:10},"min":{$gte:0,$lte:1},"s":{$gte:0,$lte:10}}).count()
	db_data = collection.find({"phid":dev_id,"datetime":{"$gte":start_date,"$lt":end_date},"s":0,"min":0})
	#print time.time() - start
	if db_data.count()==0:
		print 'no data'
		return 0
	else:
		print db_data.count()		

	return db_data
	#return mongo_dumps(db_data)

def get_data_timespan_db_index_query(dev_id,start_date,end_date,celc):
        return_list=[]
        connection = Connection()
        db = connection.lws
        collection = db.tempData
	start_date = parse_date(start_date)
	end_date = parse_date(end_date)
	start_dt_obj = datetime.datetime(start_date['year'],start_date['month'],start_date['day'])
	end_dt_obj = datetime.datetime(end_date['year'],end_date['month'],end_date['day'])
	print start_dt_obj
	print end_dt_obj
        #import time
        #start = time.time()
        #db.tempData.find({"h":{$gte:1,$lte:10},"min":{$gte:0,$lte:1},"s":{$gte:0,$lte:10}}).count()
        #db_data = collection.find({"phid":dev_id,"datetime":{"$gte":start_date,"$lt":end_date},"s":0,"min":0})
        #db_data = collection.find({"phid":dev_id,"date":{"$gte":start_dt_obj,"$lt":end_dt_obj},"h":{"$gte":start_date['hour'],"$lt":end_date['hour']},"min":{"$gte":start_date['min'],"$lt":end_date['min']},"s":{"$gte":start_date['second'],"$lt":end_date['second']}})
	db_data = collection.find({"phid":dev_id,"date":{"$gte":start_dt_obj,"$lt":end_dt_obj}})
	#print time.time() - start
        if db_data.count()==0:
                print 'no data'
                return 0
        else:
                print db_data.count()

        return db_data
        #return mongo_dumps(db_data)

#parses the date that is passed
def parse_date(date):
	return_dict = {}
	return_dict['month']=int(date[:2])
	return_dict['day']=int(date[2:4])
	return_dict['year']=int(date[4:8])
	return_dict['hour']=int(date[8:10])
	return_dict['min']=int(date[10:12])
	return_dict['second']=int(date[12:14])
	
	return return_dict


def run():
	#data = get_day_dev_info('402c8efa')
	data = get_current_stats('402c8efa',0)		
	dev_info = data['dev_info']
	data_list = data['data_list']

	
	print data_list["sensor_data"]
	
	#print get_last_checkin('402c8efa')

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
	#print parse_date('03302013150744')
	start_date = parse_date('02072013150744')
	end_date = parse_date('03072013150744')
	#print end_date
	devid = '1b7239de'
	celc = False
	import datetime
	import time
	print "Running the ISO Datetime range Query:"
	start = time.time()
	#datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
	#print start_date
	start_date = datetime.datetime(start_date['year'],start_date['month'],start_date['day'],start_date['hour'],start_date['min'],start_date['second'])
	end_date = datetime.datetime(end_date['year'],end_date['month'],end_date['day'],end_date['hour'],end_date['min'],end_date['second'])
	print start_date
	print end_date
	get_data_timespan_db_date_query(devid,start_date,end_date,celc)
	print time.time() - start
	print "Running the Indexed Date Range Query:"
	start = time.time()
	start_date = '02072013150744'
        end_date = '03072013150744'
	get_data_timespan_db_index_query(devid,start_date,end_date,celc)
	print time.time() - start
