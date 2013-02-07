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

### post_value_change(change_structure)

Posts a change in values that comes from the widget device. The following structure is put into the database in the tempData collection
info:<br>
       {<br>
         'd':date<br>
         'h':hour<br>
         'm':minute<br>
         's':second<br>
         'hs':hoursecond<br>
         'val':value<br>
         'phid':phidgetid<br>
         'sensor_data':sensor_data{} //data dictionary with all the sensor data<br>
       }

Takes in the structure seen above.

### device_registered(dev_reg)

Checks the database to see if a specific deviceid has been registered. Returns True if it has, false if it has not.

Takes in a structure with the device registration information in it.

### check_current_ip(dev_reg)


Depreciated. Only works for local aggregation nodes. Checks the current IP of the device(normally a class C/Private IP) and if its not the same, changes it.

Takes in the device registration structure.

### list_all_devices()


Lists all of the devices that are currently communicating with this aggregation node. Pulls  all of the tuples from the devices collection, removes the mongodb generated "ObjectID" string and returns a list of dicts with each devices and its information in it.

### dump_value_data()

Not really in use at this point, just dumped all of the data from the mongodb.

lws_server_main
---------------
Dependencies: Flask, db_interface(#db_interface)

Serves up the RESTful functions for the aggregation node.

* [register_new_device](#register_new_device)
* [value_change](#value_change)
* [show_all_devices](#show_all_devices)
* [home_test](#home_test)

### register_new_device()
URL: /devices/register

Method = PUT

Registers a new device. Reads in a JSON structure and checks if the device has been registered and if the IP address is current(a functionality that was originally thought that was necessary. Isn't really necessary anymore.). 

Returns '_dev_registered' if the device has been newly registered
Returns '_dev_registered' if the device has been previously registered.
Returns '_not_possible' if 'Content-Type' headers are set incorrectly.
Returns '_register_here' navigated too(GET request)

### value_change()
URL: /devices/update/value

Method: PUT

Registers value changes with the database. 

Returns '_data_put' if the data was inserted into the database successfully.
Returns '_data_fail' if the data was not inserted into the database successfully.

### show_all_devices()
URL: /devices/all

Method: GET

Renders a template that displays all of the devices registered with this particular aggregation node.

### home_test()
URL: /

Method: GET

Returns 'Hello, brew'


lws_server_main.wsgi
--------------------

wsgi script for running the server persistently.