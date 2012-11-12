#The main server runfile for the lws project

from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)

#serve up the homepage for the entire project
@app.route('/')
def index():
	return 'Homepage for the lws project.'

#serves up the about page for the entire project
@app.route('/about')
def about_project():
	return 'About page for the lws project.'

#serves up the wiki for the project
@app.route('/wiki')
def wiki_project():
	return 'Wiki page for the lws project.'

#for registering a new device.. will build XML on the backend
#with this somehow
@app.route('/devices/resgister/new')
def register_new_device():
	return 'Register a new device'

#for getting changes in temperature a normal URI will look like:
#will take in as a JSON, coming from the client
@app.route('/devices/updates/temp', methods = ['POST'])
def temp_change():	
	if request.headers['Content-Type'] == 'application/json':
		#we want to write the JSON request to a file for now so it can be served up by the temperature page
		
		return json.dumps(request.json)
	else:
		return 'something went wrong!'

#a temperature page that that the user can access current temperatures
#at- for testing pruposes only
@app.route('/temperature')
def get_temp():
		



if __name__ == '__main__':
	#turn on debugging mode for the server
	app.debug = True
	app.run()



