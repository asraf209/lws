#The main server runfile for the lws project

from flask import Flask, render_template
from flask import request
from flask import json
from flask import redirect
from db_interface import post_value_change, device_registered, get_day_dev_info,update_device
from db_interface import register_device, check_current_ip, list_all_devices
from db_interface import get_current_stats, device_checkin, get_data_timespan, get_data_timespan_db_index_query
from db_interface import define_response, get_response, get_data_timespan_db_date_query
from lws_server_sensor_config import transpose_to_strings, convert_to_real_values
from lws_server_main_zeromq import ThreadedServer
import threading

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
		return_val = device_checkin(json_struct)
		post_value_change(json_struct)
		#print json_struct
		#device_checkin(json_struct)
		if return_val == 0:
			return '_data_put'
		else:
			return return_val
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
		#day_records = get_day_dev_info(devid)
		now_record = get_current_stats(devid,0)
		dev_info = now_record['dev_info']
		#print dev_info
		now_record = now_record['data_list']
		#print now_record
		now_sense_data = now_record['sensor_data']		
		#now_sense_data ={'test':'test'}	
		
		#for thing in now_sense_data:
			#now_sense_data[str(thing)] = now_sense_data[thing]
			#del now_sense_data[thing]
		#now_sense_data = dict((k.encode('ascii'), str(v)) for (k, v) in now_sense_data.items())
		now_sense_data = transpose_to_strings(now_sense_data)
		#print now_sense_data
		now_sense_data = convert_to_real_values(now_sense_data,False,True)		

		#print now_sense_data
		#now_sense_data= {'help':0}

		return render_template('device.html', dev_info = dev_info,current_record = now_record,sensor_data = now_sense_data)	
		#return render_template('device.html')

	else:
		return 0

@app.route('/devices/device/data/time/json', methods=['GET'])
def device_data_time():
	devid = request.args['devid']
	start_date = request.args['startdate']
	end_date = request.args['enddate']
	celc = request.args['celc']
	#print start_date
	#print end_date
	#return 'hey!'
	return get_data_timespan_db_date_query(devid,start_date,end_date,celc)

@app.route('/devices/identify')
def device_identify():
        devid = request.args['devid']
	#define_response(devid, identify,thresholds,cmd)
	define_response(devid,True,0,0)
	return redirect('/devices/all')
	#return 'Identifying device!'	

@app.route('/devices/device/settings/changes', methods=['POST'])
def device_changes():
	devid = request.args['devid']
	if request.method == 'POST':
		#return request
		#return devid
		#request.form['group']	
		try:	
			sensor_name = request.form['sensor_name']
			sensor_location = request.form['sensor_location']
			sensor_group = request.form['group']
			update_dict = {'sensor_name':sensor_name,'sensor_location':sensor_location,'sensor_group':sensor_group}
			update_device(devid,update_dict)
		except:
			return redirect('/devices/all')
		#sensor_notes = request.form['sensor_description']
		return redirect('/devices/all')
		#return 'Getting changes for device %s'%devid		

	#request.form['Group']
	#request.form['Name']
	#request.form['Location']
	#request.form['Notes']	

	return "GETTING CHANGES!"

@app.route('/devices/device/settings')
def device_settings():
	print "Get settings here"
	return 'HAII'

@app.route('/devices/device/settings/json',methods=['GET'])
def device_settings_json():
	print "Get the json settings here"

#returns information about a specific device as a JSON structure. Everything that is found on the device page can be returned in a JSON structure
@app.route('/devices/device/json')
def show_device_json():
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
	



