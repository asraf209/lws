
lws Worklog
========

The focus of this is setting up the nodes and widgets. The aggregation node is maintained by us and does not necessarily need very much configuration. Some limited documentation about the aggregation node is available here as well as in the lws/aggregation/README.md file.

Table of Contents
-----
* [1 - Hardware](#hardware)
* [2 - Setup](#setup)
* [3 - URL](#URL)
* [4 - Aggregation](#aggregation)
* [5 - Database](#database)
* [6 - Misc](#misc)

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

The quick start guide for the Pi can be found here(#http://www.raspberrypi.org/quick-start-guide). You can also find more information about how to set up the Pi and get up and running in the Setup(#Setup) section.<br/>




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