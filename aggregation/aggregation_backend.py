#Backend methods/functions for the aggregation node
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#builds a graph as 
def make_graph(x,y):
	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(x,y)


#builds lists of sensors based on the sensor dict that is passed to it
def build_sensor_lists(sensor_dict):
	return 0
	

