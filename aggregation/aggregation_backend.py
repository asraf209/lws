#Backend methods/functions for the aggregation node
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#builds a graph as 
def make_graph(x,y):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(x,y)

	

