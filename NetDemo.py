from matplotlib import pyplot as plt
import networkx as nx
class DAGMeta:
    def __init__(self, layer_sizes, bbox=(.1, .1, .9, .9)):
        '''
        参数
        ==========
        bbox: DAG 所在矩形区域
        layer_sizes: DAG 每层的节点数
        '''
        self.bbox = bbox
        self.layer_sizes = layer_sizes

    @property
    def w(self):
        '''DAG 的画布宽度'''
        return self.bbox[2] - self.bbox[0]

    @property
    def h(self):
        '''DAG 的画布高度'''
        return self.bbox[3] - self.bbox[1]

    @property
    def x_center(self):
        '''DAG 的画布水平中心'''
        return (self.bbox[2] + self.bbox[0]) / 2

    @property
    def y_center(self):
        '''DAG 的画布竖直中心'''
        return (self.bbox[3] + self.bbox[1]) / 2

    def __len__(self):
        '''DAG 的层数'''
        return len(self.layer_sizes)

    @property
    def x_spacing(self):
        '''DAG 水平方向的留白间隙'''
        return self.w / (len(self) - 1)

    @property
    def y_spacing(self):
        '''DAG 竖直方向的留白间隙'''
        return self.h / max(self.layer_sizes)

class SlowlyDAG(DAGMeta):
    def plot(self):
        import random
        G = nx.DiGraph()
        node_count = 0
        for i, v in enumerate(self.layer_sizes):
            layer_top = self.y_spacing * (v - 1) / 2. + self.y_center
            for j in range(v):
                G.add_node(node_count, pos=(self.bbox[0] + i * self.x_spacing, layer_top - j * self.y_spacing))
                node_count += 1

        for x, (left_nodes, right_nodes) in enumerate(zip(self.layer_sizes[:-1], self.layer_sizes[1:])):
            for i in range(left_nodes):
                for j in range(right_nodes):
                    G.add_edge(i + sum(self.layer_sizes[:x]), j + sum(self.layer_sizes[:x + 1]))

        pos = nx.get_node_attributes(G, 'pos')
        # 把每个节点中的位置pos信息导出来
        nx.draw(G, pos,
                node_color=range(node_count),
                with_labels=True,
                node_size=500,
                edge_color=[random.random() for i in range(len(G.edges))],
                width=2,
                font_color='black',
                cmap=plt.cm.Paired,  # matplotlib 的调色板，可以搜搜，很多颜色呢
                edge_cmap=plt.cm.Blues)
        plt.show()
bbox = .1, .1, .9, .9  # 网络所在矩形区域
layer_sizes = [4, 7, 5, 2]  # 网络每层的节点数
self = SlowlyDAG(layer_sizes, bbox)
self.plot()