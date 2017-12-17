import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint


# Adding our own node names
nodenames = ['ajc', 'trez', 'chacko', 'sucy', 'teena','jjk']
# defined graph
G = nx.complete_graph(len(nodenames))
total_nodes = len(G.nodes())
mapping = {i: nodename for i, nodename in enumerate(nodenames)}
#now mapping looks like {0:'ajc', 1:'trez', ...}
H = nx.relabel_nodes(G, mapping)

edge_disjoint_paths = []
edges = []
for node_num in xrange(total_nodes-1):
    nodecnt_inpath = total_nodes+1
    while nodecnt_inpath > 1:
        paths = [path for path in nx.all_simple_paths(
                    H, nodenames[node_num], nodenames[node_num],
                    cutoff=nodecnt_inpath)
                 if len(path) == nodecnt_inpath]
        # print paths
        # print len(paths), total_nodes

        for path in paths:
            tmp_edges = []
            for i in xrange(len(path)-1):
                edge = {path[i], path[i+1]}
                if edge in edges:
                    break
                tmp_edges.append(edge)
            else:
                edges.extend(tmp_edges)
                edge_disjoint_paths.append(path)
        nodecnt_inpath -= 1

pprint(edge_disjoint_paths)

# pos=nx.spring_layout(H)
#
# nx.draw_networkx_edges(H, pos, width=1.0,alpha=0.5)
# nx.draw_networkx_labels(H, pos, font_size=16)
# nx.draw_networkx_nodes(H, pos, node_color='c', font_size=16)
#
# plt.axis('off')
# plt.show()
