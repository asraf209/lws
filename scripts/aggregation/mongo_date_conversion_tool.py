from pymongo import Connection
import datetime
import json
from bson.json_util import dumps as mongo_dumps
import time

connection = Connection()
from_db = connection.lws
to_db = connection.lws_date
from_collection = from_db.tempData
to_collection = to_db.tempData

from_db_data = from_collection.find()
print from_db_data.count()
start = time.time()
count = 0
for thing in from_db_data:
	if count == 1000:
		break
	else:
		#count +=1
		new_data = json.loads(mongo_dumps(thing))
		#date_obj = datetime.date(new_data['y'],new_data['month'],new_data['d'])
		try:
			print new_data	
			date_time_obj = datetime.datetime(new_data['y'],new_data['month'],new_data['d'],new_data['h'],new_data['min'],new_data['s'])
			date_obj = datetime.datetime(new_data['y'],new_data['month'],new_data['d'])
			#print date_time_obj
			new_data['datetime'] = date_time_obj
			new_data['date'] = date_obj
			to_collection.insert(new_data)
		except:
			print 'exception'

		#print date_obj
		#print new_data

print time.time() - start
#connection.commit()
#to_db.commit()
	
	
