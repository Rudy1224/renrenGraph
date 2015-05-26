import cPickle as pickle
import networkx as nx
import matplotlib.pyplot as plt
import sys, time

f = open('relations.pkl', 'rb')
d = pickle.load(f)
    
#leave only my friends
for fuid in d[471872181]:
    d[fuid] = filter(lambda x: x in d[471872181], d[fuid])

#draw graph
G = nx.Graph()

for stem in d.keys():        
    for leaf in d[stem]:
        G.add_edges_from([(stem, leaf)])

#remove isolated nodes
##G.remove_nodes_from([key for key in nx.degree(G) if nx.degree(G)[key]<=3])

nx.draw(G,
        node_size = map(lambda x:2*nx.degree(G)[x], nx.nodes(G)),
        node_color = map(lambda x:nx.degree(G)[x], nx.nodes(G)),
        alpha=0.5, width=0.1)

plt.show()
