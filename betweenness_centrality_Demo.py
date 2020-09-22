import networkx as nx
from pylab import show
from sorted_map import sorted_map
from netDemo_4 import core_50

g=nx.Graph()
g.add_edge('G',"F")
g.add_edge('G','E')
g.add_edge('G','D')
g.add_edge('E','F')
g.add_edge('D','A')
g.add_edge('E','D')
g.add_edge('F','D')
g.add_edge('D','B')
g.add_edge('D','C')
g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('A','C')
nx.draw(g)
#show()
bc=nx.betweenness_centrality(g)
bc_sorted=sorted_map(bc)
print(bc_sorted)
bc_Russia=nx.betweenness_centrality(core_50)
bc_Russia_sorted=sorted_map(bc_Russia)
print(bc_Russia_sorted[:10])
