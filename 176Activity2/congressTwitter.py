#2 Graph of Congress Twitter
import networkx as nx
import matplotlib.pyplot as plt

edgelist_file = 'congress.edgelist'
G = nx.read_edgelist(edgelist_file)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()