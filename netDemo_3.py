import networkx as nx
from pylab import show
from netDemo_2 import read_friends

def snowball_sampling(g,center,max_depth=2,current_depth=0,visited=[]):
    if current_depth==max_depth:
        print(f"out of depth!:{center}")
        return visited
    if center in visited:
        return visited
    visited.append(center)
    read_friends(g,center)
    for neighbors in g.neighbors(center):
        visited=snowball_sampling(g,neighbors,max_depth=max_depth,current_depth=current_depth+1,visited=visited)
    return visited

g=nx.Graph()
snowball_sampling(g,center="valerois")
nx.write_pajek(g,"test_1.net")
#nx.write_pajek(g,"lj_read_1.net")
#nx.draw(g)
#show()