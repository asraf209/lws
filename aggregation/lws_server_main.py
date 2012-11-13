#The main server runfile for the lws project

from flask import Flask
from flask import request
from flask import json
from db_interface import post_temp_change

app = Flask(__name__)

#for registering a new device.. will build XML on the backend
#with this somehow
@app.route('/devices/resgister/new')
def register_new_device():
	return 'Register a new device'

#for getting changes in temperature a normal URI will look like:
#will take in as a JSON, coming from the client
@app.route('/devices/updates/temp', methods = ['PUT'])
def temp_change():	
	if request.headers['Content-Type'] == 'application/json':
		#We will post the temperature change here, using
		#the database interface file that has been written				
		post_temp_change(request.json)
		
	else:
		return 'something went wrong!'

#a temperature page that that the user can access current temperatures
#at- for testing pruposes only
@app.route('/temperature')
def get_temp():
	return 'Hii'			


if __name__ == '__main__':
	app.debug = True
	app.run()



