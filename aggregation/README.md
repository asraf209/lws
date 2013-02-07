Aggregation node modules
========================

Modules
-----------------
* [1 - aggregation_backend](#aggregation_backend)
* [2 - db_interface](#db_interface)
* [3 - lws_server_main](#lws_server_main)
* [4 - lws_server_main.wsgi](#lws_server_main.wsgi)
* [5 - misc](#misc)


aggregation_backend
-------------------
Dependencies: none.

Depreciated. Originally where miscellaneous backend operations were going to be kept. 

db_interface
------------

Dependencies: pymongo, datetime

Where all of the functions for database manipulations are housed:

* [post_value_change](#post_value_change)
* [device_registered](#device_registered)
* [check_current_ip](#check_current_ip)
* [list_all_devices](#list_all_devices)
* [dump_value_data](#dump_value_data)

post_value_change
---
Posts a change in values that comes from the widget device. The following structure is put into the database in the tempData collection
info:
       {
         'd':date
         'h':hour
         'm':minute
         's':second
         'hs':hoursecond
         'val':value
         'phid':phidgetid
         'sensor_data':sensor_data{} //data dictionary with all the sensor data
       }

### device_registered


Checks the database to see if a specific deviceid has been registered. Returns True if it has, false if it has not.

### check_current_ip


Depreciated. Only works for local aggregation nodes. Checks the current IP of the device(normally a class C/Private IP) and if its not the same, changes it.

### list_all_devices


Lists all of the devices that are currently communicating with this aggregation node. Pulls  all of the tuples from the devices collection, removes the mongodb generated "ObjectID" string and returns a list of dicts with each devices and its information in it.

### dump_value_data

Not really in use at this point, just dumped all of the data from the mongodb.