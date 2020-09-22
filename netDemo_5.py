import networkx as nx

def trim_degrees(g,degree=1):
    g2=g.copy()
    deg=nx.degree(g2)
    for node in g.nodes():
        if deg[node]<=degree:
            g2.remove_node(node)
    return g2