import math

#module that configures which ports the sensors are one
sensor_pos = {'0':'_nothing','1':'_nothing','2':'_nothing','3':'Sound Sensor','4':'Light Sensor','5':'Motion Sensor','6':'Humidity Sensor','7':'Temperature Sensor'}

#adds the sensor location strings to the incoming dict based on the sensor positions
def transpose_to_strings(dict):
	return_dict = {}
	for key in dict:
		if sensor_pos[key] == '_nothing':
			pass
		else:
			return_dict[sensor_pos[key]] = dict[key] 

	return return_dict

#converts to real world values
def convert_to_real_values(dict,c,f):
	for key in dict:
		if key == 'Sound Sensor':
			dict[key] = get_sound_db(dict[key])
		if key == 'Humidity Sensor':
			dict[key] = get_humidity(dict[key])
		if key == 'Temperature Sensor':
			dict[key] = get_temp(dict[key],c,f)
	return dict	

def get_humidity(raw_value):
	return (float(raw_value)*.1906)-40.2

def get_temp(raw_value,c,f):
	if c:
		return get_temp_c(raw_value)
	if f:
		return get_temp_f(raw_value)	

def get_temp_c(raw_value):
	return (float(raw_value)*.22222)-61.11

def get_temp_f(raw_value):
	return (get_temp_c(raw_value)*9)/5 +32

def get_sound_db(raw_value):
	return 16.801*math.log(float(raw_value))+9.872


sense_test= {'Humidity Sensor': '341', 'Light Sensor': '2', 'Temperature Sensor': '370', 'Sound Sensor': '14', 'Motion Sensor': '512'}
print convert_to_real_values(sense_test,False,True)
