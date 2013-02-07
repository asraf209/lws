
lws Worklog
========

The focus of this is setting up the nodes and widgets. The aggregation node is maintained by us and does not necessarily need very much configuration. Some limited documentation about the aggregation node is available here as well as in the lws/aggregation/README.md file.

![hardwarestack](https://raw.github.com/t3hpaul/lws/blob/gh-pages/static/worklog_photos/full_stack_flash.jpg)

Table of Contents
-----
* [1 - Hardware](#hardware)
* [2 - Setup](#setup)
* [3 - URL](#URL)
* [4 - Aggregation](#aggregation)
* [5 - Database](#database)
* [6 - Misc](#misc)
* [7 - Sensor Positions](#sensor-positions)

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

<b> Humidity Sensor <b/><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1125_0)

* Measures Relative Humidity from 10% to 95%
* Operates over 0% to 100% Relative Humidity

<b> Temperature Sensor </b><br/>
The official Phidget documentation can be found [here] (#http://www.phidgets.com/products.php?category=6&product_id=1125_0)

* Accurately measures ambient temperatures from -30°C to +80°C (-22°F to 176°F) 
* Typical error of ±0.75 degrees Celsius in the 0°C to 100°C range

<b> Some pictures of our Phidgets and sensors </b><br>


### Aggregation

Currently, the aggregation node is hosted on a virtual machine running Ubuntu Server 12.04 LTS. We are planning on moving all of the code and databases to a SaaS cloud service such as Heroku(http://www.heroku.com/). We are also investigating Cloud Foundry and Amazon Web Services. Heroku's free platform and support for our software stack makes it the 

Setup
-----


URL
---

Aggregation
-----------

Database
--------

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
