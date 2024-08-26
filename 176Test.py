import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

nx.draw(G)


import matplotlib.pyplot as plt
plt.show()

print("Betweeness Centrality")
print(nx.betweenness_centrality(G))
print("\n")