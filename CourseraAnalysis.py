import networkx as nx
import csv
from pylab import show
#生成图
g=nx.Graph()
#打开第一个文件
with open("C:\\Users\\72493\\Desktop\\virology-1.csv",encoding="utf-8-sig") as csv_file:
    content=csv.reader(csv_file)
    for line in content:
        #防止重复边以及重复节点
        if tuple(line) not in g.edges and line[0]!=line[1] and line[0]!='' and line[1]!='':
            g.add_edge(line[0], line[1])

#打开第二个文件
with open("C:\\Users\\72493\\Desktop\\virology-2.csv",encoding="utf-8-sig") as csv_file:
    content=csv.reader(csv_file)
    for line in content:
        if tuple(line) not in g.edges and line[0]!=line[1] and line[0]!='' and line[1]!='':
            g.add_edge(line[0], line[1])

#输出.gexf文件
nx.write_gexf(g,"C:\\Users\\72493\\Desktop\\output-virology.gexf")

#输出csv文件
with open("C:\\Users\\72493\\Desktop\\output-virology.csv",mode='w',encoding="utf-8-sig") as f:
    writer=csv.writer(f)
    writer.writerows(g.edges)
