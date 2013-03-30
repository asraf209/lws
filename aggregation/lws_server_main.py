#The main server runfile for the lws project

from flask import Flask, render_template
from flask import request
from flask import json
from db_interface import post_value_change, device_registered, get_day_dev_info
from db_interface import register_device, check_current_ip, list_all_devices
from db_interface import get_current_stats, device_checkin

app = Flask(__name__)

def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string

#for registering a new device
@app.route('/devices/register', methods = ['PUT'])
def register_new_device():
	if request.headers['Content-Type'] == 'application/json':
		#Check if device is already registered
		if device_registered(request.json):
			#include external IP address check here!! <!>!<>!<>!<>!<>!<!>
			check_current_ip(request.json)
			#add device checkin here
			return '_dev_prev_registerd'
		#If the device isn't registered, we register it with the registration database 
		else:
			register_device(request.json)
			#add device checkin here	
			return 	'_dev_registered'
	else:
		return '_not_possible'	
	return '_register_here'

#for getting changes in temperature a normal URI will look like:
#will take in as a JSON, coming from the client
@app.route('/devices/updates/value', methods = ['PUT'])
def value_change():	
	if request.headers['Content-Type'] == 'application/json':
		#We will post the value change here, using
		#the database interface file that has been written				
		json_struct = request.json
		#print json_struct
		#print json.loads(json_struct)
		device_checkin(json_struct)
		post_value_change(json_struct)
		#print json_struct
		#device_checkin(json_struct)
		return '_data_put'
	else:
		return '_data_fail'

#setup for all of the devices that we have running
@app.route('/devices/all')
def show_all_devices():
	return render_template('devices.html', all_devices=list_all_devices())

#Returns information about a device
@app.route('/devices/device')
def show_device():
	if 'devid' in request.args:
		devid = request.args['devid']
		day_records = get_day_dev_info(devid)
		now_record = get_current_stats(devid,0)
		dev_info = now_record['dev_info']
		#print dev_info
		now_record = now_record['data_list']
		#print now_record
		now_sense_data = now_record['sensor_data']		
		#now_sense_data ={'test':'test'}	
		
		for thing in now_sense_data:
			now_sense_data[str(thing)] = now_sense_data[thing]
			#del now_sense_data[thing]
		now_sense_data = dict((k.encode('ascii'), str(v)) for (k, v) in now_sense_data.items())
		
		#print now_sense_data
		#now_sense_data= {'help':0}

		return render_template('device.html', dev_info = dev_info,current_record = now_record,sensor_data = now_sense_data)	
		#return render_template('device.html')

	else:
		return	
	
	#return render_template('device.html')

@app.route('/devices/device/changes', methods=['PUT'])
def device_changes():
	print "GETTING CHANGES!"

#returns information about a specific device as a JSON structure. Everything that is found on the device page can be returned in a JSON structure
@app.route('/devices/device/json')
def showd_device_json():
	return 0


#testing the template rendering
@app.route('/template/test')
def template_test():
	return render_template('index.html')

@app.route('/')
def home_test():
	return render_template('index.html')
	#return 'Hello, brew'

@app.route('/login')
def login_user():
	return 'Nothing here now.'

@app.route('/users/register')
def register_user():
	return 'Nothing here now.'


if __name__ == '__main__':
	app.debug = True
	app.run()



