import networkx as nx
from sorted_map import sorted_map
import csv

g=nx.Graph()
with open("C:\\Users\\72493\\Desktop\\9.25日毛数据\\dsp-1.csv",encoding="utf-8-sig") as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        g.add_edge(line[0],line[1])

pr=nx.pagerank(g)
print(sorted_map(pr)[:10])