# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:18:45 2021

@author: LiuHang
"""

import json
import networkx as nx

#G = nx.Graph()
G = nx.DiGraph()

#path = 'D:/git/NetworkGraph-master/index/index_static/data/public_data/带自环.json'
path = 'C:/Users/LiuHang/Downloads/demo1.json'
edge_list = []
node_set = set()
with open(path, 'rb') as file:
    data = file.read()
    js = json.loads(data)
    for link in js['links']:
        n1 = int(link['source'])
        n2 = int(link['target'])
        node_set.add(n1)
        node_set.add(n2)
        edge = (n1, n2)
        edge_list.append(edge)

G.add_nodes_from(range(0, len(node_set)))
G.add_edges_from(edge_list)
#A = nx.to_numpy_matrix(G)
A = nx.adjacency_matrix(G).todense()
#print(A)

MA = A.astype(object)
for link in js['links']:
    s = int(link['source'])
    p = str(link['label'])
    o = int(link['target'])
    MA[s, o] = p
print(MA)
