from flask import Flask
from phidget_poller import get_current_temp

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world!'

#gets a current reading of some sensor that is defined by the GET parameter passed.
#returns a json data structure 
@app.route('/current/')
def current_temp():
	if 'sens_id' in request.args:
		return get_current(request.args['sense_id']
	else:
		return 'Null'


if __name__ == '__main__':
	app.run()
