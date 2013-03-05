
lws Worklog
========

The focus of this is setting up the nodes and widgets. The aggregation node is maintained by us and does not necessarily need very much configuration. Some limited documentation about the aggregation node is available here as well as in the lws/aggregation/README.md file.


![hardwarestack](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/phidgetio.jpg)

![hardwarestack](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/full_stack_flash.jpg)


Table of Contents
-----
* [1 - Hardware](#hardware)
* [2 - Setup](#setup)
* [3 - URL](#URL)
* [4 - Aggregation](#aggregation)
* [5 - Database](#database)
* [6 - Misc](#misc)
* [7 - Sensor Positions](#sensor-positions)
* [8 - Troubleshooting](#troubleshooting)

Hardware
------------

Our hardware stack is broken down into two main sections:
* [Widgets/Nodes] (#Widgets/Nodes)
* [Aggregation] (#Aggregation)

### Widgets/Nodes

<b>Host Device</b><br/>
The purpose of the host device is collect data from the sensors, package it up and send it off to the aggregation node. In the future we may attempt to get the nodes to do some distributed computing for data analysis of the data collected. <br/>

We opted to use Raspberry Pi's for the host device. The small form factor, processing power, lower power consumption, ease of use, and variety of options for development platforms made them the best host device for this project. <br/>

<b>Raspberry Pi Tech Specs</b><br/>
* Broadcom BCM2835 system on a chip (SoC)
* ARM1176JZF-S 700 MHz processor
* VideoCore IV GPU
* 512MB of RAM
* SD card for booting and long-term storage (we are using an 8GB Kingston SD card)<br/>

The quick start guide for the Pi can be found [here] (#http://www.raspberrypi.org/quick-start-guide). You can also find more information about how to set up the Pi and get up and running in the [Setup] (#Setup) section.<br/>

A few shots of one of our Raspberry Pi's:

![raspberry1](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/pi1.jpg)<br/>
![raspberry2](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/pi_side.jpg)<br/>
![raspberry3](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/pi_top.jpg)<br/>


<b>Sensing</b><br/>

For collecting environmental data, we obviously need some sort of sensors. Since we also want to eventually control some of the environment that the widgets/nodes are deployed in, we opted to use Phidgets.<br/>

Phidgets provide an easy way to interface with sensors through an API as well as throughout the ability to have analog inputs for custom sensing applications. Additionally, Phidget I/O boards include analog outputs; this allows us to control other devices. <br/>

Phidgets are broken into two main parts; I/O boards and Sensors. <br/>

<b>PhidgetInterfaceKit 8/8/8 - I/O Board </b><br/>
* 8 Analog Inputs with configurable data acquisition rates
* 8 Digital Inputs with hardware noise filtering
* 8 Digital Outputs
* 5V terminal block besides Analog Input 7 and Digital Output 7

<b> Sound Sensor </b><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1133_0)
* Measures sound pressure level (SPL) between 50db to 100dB
* Frequency range of 100Hz to 8kHz

<b> Light Sensor </b><br/>

The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1127_0).

* Measures human perceptible light level in lux
* Measures from 1 lux to 1000 lux

<b> Motion Sensor </b><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=5&product_id=1111_0).

* Detects changes in infrared radiation which occur when there is movement
* Narrow sensing area.

<b> Humidity Sensor </b><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1125_0)

* Measures Relative Humidity from 10% to 95%
* Operates over 0% to 100% Relative Humidity

<b> Temperature Sensor </b><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1125_0)

* Accurately measures ambient temperatures from -30°C to +80°C (-22°F to 176°F) 
* Typical error of ±0.75 degrees Celsius in the 0°C to 100°C range

<b> Some pictures of our Phidgets and sensors </b><br>

![phidgetioboard](https://raw.github.com/t3hpaul/lws/master/static/worklog_photos/phidgetio.jpg)

### Aggregation

Currently, the aggregation node is hosted on a virtual machine running Ubuntu Server 12.04 LTS. We are planning on moving all of the code and databases to a SaaS cloud service such as [Heroku](#http://www.heroku.com/). We are also investigating Cloud Foundry and Amazon Web Services. Heroku's free platform and support for our software stack makes it the 

Setup
-----
Setup of the Pi's + development software will be here. Anything that pertains to the aggregation node will be documented pretty extensively at a later date. 

Setting up the nodes for development is a relatively simple process that consists of a few simple steps:

* 1 - Setting up the Pi
* 2 - Installing dependencies
* 3 - Getting the code
* 4 - Running the code
* 5 - Registering your device

<b> 1 - Setting up the Pi </b> <br>
Assuming you have all of the proper hardware, you need to set up your Pi. 

Start with flashing your SD card(if you didn't purchase an SD card pre-loaded with Debian)

Flashing information can be found [here](#http://elinux.org/RPi_Easy_SD_Card_Setup). There are instructions for Windows, OS X, and Linux systems there.

The image that we have been testing and that works well is [here](#http://downloads.raspberrypi.org/images/raspbian/2013-02-09-wheezy-raspbian/2013-02-09-wheezy-raspbian.zip)

Once you have the image flashed, go ahead and boot up your Pi. It should be able to boot headlessly and you should be able to ssh into it using the following parameters:

<b> Hostname: </b> raspberrypi<br>
<b> Username: </b> pi <br>
<b> Password: </b> raspberry<br>

Alternatively, you can plug it into a display and configure it that way.

Once you ssh into the Pi, you can run ```raspi-config``` and continue setup.

You need to configure the following:
* Enable SSH access
* Change the password
* Expand the root partition to the entire SD card(option)
* Set the timezone

<b> Finally, you should get an update and install git to clone our code! </b> <br>

Update:

```
apt-get update
```

Git:

```
apt-get install git
```

<b> 2 - Installing Dependencies </b>

Since we are using the Phidgets for a agile and rapid prototype development style, we need to get a few things set up for them to work on your Pi. Make sure that you run the following commands as the root user. 

<b> Note that you can also do the same with the Phidgets plus any Unix host device with a network connection! </b><br>

More detailed instruction for setting up the dependencies for the Phidgets can be found [here](#http://www.phidgets.com/docs/OS_-_Linux)

A script that will do everything mentioned here, and more can be found [here](#
https://raw.github.com/t3hpaul/lws/master/scripts/raspberrysetup.sh)

The usb linux library needs to be installed:

```
apt-get install libusb-1.0-0-dev
```

Next, we need to install the Phidget Libraries:

Downloads them then unpack them, first:
```
wget http://www.phidgets.com/downloads/libraries/libphidget.tar.gz
tar -xzvf libphidget.tar.gz 
```
I like to clean up while I work:
```
rm libphidget.tar.gz
```
Go ahead and install the libraries:
```
cd libphidget-2.1.8.20121218/
./configure
make
make install
```
Again, I like to clean up:
```
cd ..
rm -r libphidget-2.1.8.20121218
```
Install the Python libraries and modules:
```
wget http://www.phidgets.com/downloads/libraries/PhidgetsPython.zip
unzip PhidgetsPython.zip
cd PhidgetsPython
python setup.py install
```

Clean up, clean up, everybody do their share:
```
cd ..
rm -r PhidgetsPython
```

The RESTful version of our code uses the super clean python Requests framework. More information on this awesome framework can be found [here](#http://docs.python-requests.org/en/latest/)


```
git clone git://github.com/kennethreitz/requests.git
cd requests
python setup.py install
cd ..
rm -r requests
```
<b> 3 - Getting the code </b><br>

Once we have the requests framework, we can clone the lws repository. We put it in /etc/lws and set it up to startup with the system.

```
git clone https://github.com/t3hpaul/lws.git /etc/lws
cat /etc/lws/scripts/initscript.sh > /etc/init.d/lwsclient
```

Sometimes we needed to give full acces to the startup/shutdown script, which is odd:

```
chmod 777 /etc/init.d/lwsclient
```

<b> 4 - Running the code </b><br>

<b> Now we can test the installation and see if it works </b><br>
```
python /etc/lws/client/lws_client_main.py
```

<b> If it does, you should see something like this: </b><br>

```
creating the interface kit
connecting to the device!
IP is: 192.x.x.x
{'s': 31, 'd': 5, 'min': 58, 'y': 2013, 'h': 13, 'devid': 'xxxxxx', 'ipaddress': 'x.x.x.x', 'month': 3}
_dev_prev_registerd
{0: 0, 1: 0, 2: 0, 3: 7, 4: 19, 5: 491, 6: 371, 7: 366}
{"s": 31, "phid": "xxxx", "d": 5, "min": 58, "y": 2013, "h": 13, "sensor_data": {"0": 0, "1": 0, "2": 0, "3": 7, "4": 19, "5": 491, "6": 371, "7": 366}, "month": 3}
_data_put
```

If it can't connect to the interface kit, then you should try running:

```
lsusb
```

If the interface kit isn't listed, reboot the Pi. If it still isn't listed, you probably have a power problem.

<b> 4 - Register the device /b><br>
Coming soon.

Misc URLS:

Config Script:
http://elinux.org/RPi_raspi-config#The_raspi-config_script

URL
---

Aggregation
-----------

Database
--------

Setting up the mongodb for the aggregation node is simple:

```
use lws
db.createCollection('deviceCheckIn')
db.createCollection('tempData')
db.createCollection('devices')
```

Misc
----

Sensor Positions
----------------
[0 - Nothing Attached]<br/>
[1 - Nothing Attached]<br/>
[2 - Nothing Attached]<br/>
[3 - Sound Sensor]<br/>
[4 - Light Sensor]<br/>
[5 - Motion Sensor]<br/>
[6 - Humidity Sensor]<br/>
[7 - Temperature Sensor]<br/>

Trouble Shooting
----------------
