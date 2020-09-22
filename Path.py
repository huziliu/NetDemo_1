from networkx import algorithms
import networkx
from networkx import *
import itertools
g=networkx.generators.krackhardt_kite_graph()
print(algorithms.shortest_path(g,5,1))
print(algorithms.dijkstra_path(g,5,1))
#print(dict(algorithms.all_pairs_shortest_path(g)))
#print(dict(algorithms.all_pairs_shortest_path(g))[5])
#并排显示
#lst1=[1,2]
#lst2=[5,6]
#print(lst1,lst2)
#print(*lst1)
nodes=list(g.nodes())[:8]
node_pairs=list(itertools.combinations(nodes,2))
#print(node_pairs)
for pair in node_pairs:
    print(algorithms.shortest_path(g,*pair),algorithms.dijkstra_path(g,*pair))
print(node_pairs)