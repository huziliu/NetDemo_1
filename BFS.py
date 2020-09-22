import networkx
from networkx import *
g=networkx.generators.krackhardt_kite_graph()
edges=bfs_edges(g,0)
print(list(edges))
successors=bfs_successors(g,0)
print(dict(successors))