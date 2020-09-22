import networkx as net
import urllib
from pylab import show

g=net.Graph()
g.add_edge('a','b')
g.add_edge('b','c')
g.add_edge('c','a')
g['a']['b']["weight"]=1
net.draw(g)
show()
print(g.nodes)
print(g.edges)
print(g['a'])