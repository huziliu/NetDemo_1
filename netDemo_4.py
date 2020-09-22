import networkx as nx
from matplotlib import pyplot as plot
from pylab import show
from netDemo_5 import trim_degrees

g=nx.read_pajek("test_1.net")
#deg=nx.degree(g)
#deg可以任意转型为dict或list
#print(list(deg))
#print(deg["valerois"])
#print((sorted(deg,key=lambda x:x[1],reverse=True))[0:10])
#h=plot.hist(dict(deg).values(),100)
#plot.loglog(h[1][1:],h[0])
#show()
'''
core_1=trim_degrees(g)
print(len(core_1))
core_2=trim_degrees(g,degree=2)
print(len(core_2))
core_3=trim_degrees(g,degree=3)
print(len(core_3))
core_4=trim_degrees(g,degree=4)
print(len(core_4))
core_5=trim_degrees(g,degree=5)
print(len(core_5))
core_6=trim_degrees(g,degree=6)
print(len(core_6))
core_7=trim_degrees(g,degree=7)
print(len(core_7))
core_8=trim_degrees(g,degree=8)
print(len(core_8))
core_9=trim_degrees(g,degree=9)
print(len(core_9))
core_10=trim_degrees(g,degree=10)
print(len(core_10))
'''
#core_20=trim_degrees(g,degree=20)
#print(len(core_20))
core_50=trim_degrees(g,degree=50)
print(len(core_50))
#nx.write_gexf(core_20,"lj_read_2.gexf")
