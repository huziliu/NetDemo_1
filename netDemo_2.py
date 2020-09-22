import networkx as nx
from urllib import request
from pylab import show

def read_friends(g,name):
    response = request.urlopen('http://www.livejournal.com/misc/fdata.bml?user='+name)
    for line in response.readlines():
        if bytes.decode(line).startswith('#'):
            continue
        parts=bytes.decode(line).split()
        if len(parts)==0:
            continue
        if parts[0]=='>':
            g.add_edge(name,parts[1])
        else:
            g.add_edge(parts[1],name)

'''
g=nx.Graph()
read_friends(g,"hutshepsut")
nx.draw(g)
show()
'''