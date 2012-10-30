#Quick and dirty parsing of the sensorConfig.xml file. Work in progress.

import xml.etree.ElementTree as etree

tree = etree.parse('sensorConfig.xml')
root = tree.getroot()

for child in root:
	print child.tag, child.attrib, child.text
