Authors: Paul Stasiuk, George K. Thiruvathukal, Konstantin Läufer from the 
Loyola University Chicago Computer Science Department.

lws
========
Current Sensor Positions
========================

[0 - Nothing Attached]<br/>
[1 - Nothing Attached]<br/>
[2 - Nothing Attached]<br/>
[3 - Sound Sensor]<br/>
[4 - Light Sensor]<br/>
[5 - Motion Sensor]<br/>
[6 - Humidity Sensor]<br/>
[7 - Temperature Sensor]<br/>

Table of Contents
-----
* [1 - Introduction](#introduction)
* [2 - Problem Description](#problem-description)
* [3 - Our Goal](#our-goal)
* [4 - Solution](#solution)
* [5 - Directory Structure](#directory-structure)

Introduction
------------

lws Is an open source initiative for the development of environmental monitors which adhere to the “Internet of Things” principles and can be easily reproduced and distributed. The purpose of the project is to promote true sustainability through the use of intelligent environmental monitoring to control various variables in various settings.


Problem description
-------------------

Quite simply; we want to be able to collect and aggregate environmental data for both inside and outside. In order to do this we want to be able to expose the sensors through a RESTful API that allows others to build interfaces and slice and dice the data however they want it.


Our goal
--------

We have a few goals, we list them here in no particular order:

* Build software and assemble the hardware in such a way that allows for it to be reproduced easily and at minimal cost.
* Build a cloud-based service that allows for the devices to be easily addressed using RESTful principles

Solution
--------

For a more comprehensive understanding of our solution, see the work loglog, we list all the steps we have taken and issues that we have run into. This is just a brief overview.

We will use Raspberry Pi's in conjunction with Phidgets to aggregate data to some cloud based aggregation node. The node will be available at http://lws.at-band-camp.net/. Currently the node is being developed on Heroku's free platform.

Directory Structure
-------------------

All that really matters is the client folder and aggregation folder. Code for the widgets can be found in the client folder and code for the aggregation node can be found in the aggregation folder. The code is generally well documented.