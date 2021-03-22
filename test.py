# Import Libraries
import pandas as pd
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite


#reading csv files
df_edges = pd.read_csv('edges_L6.csv')
df_nodes = pd.read_csv('nodes_l6.csv')

#initialize graph
G = nx.Graph()

#find edges
def ObtainEdges(df):
    edges_list = [];
    for index, info in df.iterrows():
        edges_list.append((info[0], info[1]))
    return edges_list

edges_list = ObtainEdges(df_edges)

# find nodes
def ObtainAttr(df):
    attr_dict = dict()
    for index, info in df.iterrows():
        attr_dict[info[0]] = info[1];
    return attr_dict

attr_dict= ObtainAttr(df_nodes)

# Task 1
#Number of Nodes in each node set
no_nodes = len(attr_dict)
print(no_nodes)

#Number of Edges in  each node set
no_edges = len(edges_list)
print(no_edges)

df_nodes_list1 = df_nodes['pol_ge_sp'].tolist()
df_nodes_list2 = df_nodes['plant_ge'].tolist()


G.add_nodes_from(df_nodes_list1, bipartite=0)
G.add_nodes_from(df_nodes_list2, bipartite=1)
G.add_edges_from(edges_list)
my_matching = bipartite.matching.hopcroft_karp_matching(G, df_nodes_list1)
print(my_matching)