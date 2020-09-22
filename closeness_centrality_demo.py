import networkx as nx
import netDemo_4
from sorted_map import sorted_map
from matplotlib import pyplot as plot
from pylab import show

c=nx.closeness_centrality(netDemo_4.core_20)
#print(c)
sorted_c=sorted_map(c)
print(sorted_c[:10])
plot.hist(dict(c).values(),100)
show()