#The main server runfile for the lws project

from flask import Flask, render_template
from flask import request
from flask import json
from db_interface import post_value_change, device_registered, get_device_info
from db_interface import register_device, check_current_ip, list_all_devices

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
			check_current_ip(request.json)
			return '_dev_prev_registerd'
		#If the device isn't registered, we register it with the registration database 
		else:
			register_device(request.json)	
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
		post_value_change(request.json)
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
	
	return render_template('device.html')

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
	return 'Hello, brew'

if __name__ == '__main__':
	app.debug = True
	app.run()



