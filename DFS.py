import networkx.generators.small
from networkx import *
g=networkx.generators.small.krackhardt_kite_graph()
#深度优先遍历
def DFS_nodes(graph,node,visited=[]):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS_nodes(graph,neighbor,visited)
    return visited

def DFS_edges(graph,node,visited=[],edges=[]):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            edges.append((node,neighbor))
            DFS_edges(graph,neighbor,visited,edges)
    return edges

'''
def DFS_edges(graph, node, visited=[], edges=[]):
    visited.append(node)
    for ni in graph[node]:
        if not ni in visited:
            edges.append((node, ni))
            DFS_edges(graph, ni, visited, edges)
    return edges
'''
print(DFS_nodes(g,0))
print(DFS_edges(g,0))
#利用NetWorkX可直接实现DFS
edges=dfs_edges(g,0)
print(list(edges))
successors=dfs_successors(g,0)
print(successors)
predecessors=dfs_predecessors(g,0)
print(predecessors)
