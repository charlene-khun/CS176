import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# 1. Degrees
# 2. Screenshots of Visualizations: Kamada Kawai, Fruchterman Reingold, Circular, Random, Spectral, Spring
# 3. Centralities: 4 kinds

G = nx.read_gml("karate.gml", label="id")

# 1. Degrees
import pandas as pd

degrees = [G.degree(n) for n in G.nodes()]
degrees.sort()
print("Degrees")
print(degrees)
print("\n")
fig, ax = plt.subplots()
data = pd.DataFrame(
    {
        "degrees1": [
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            5,
            5,
            5,
            6,
            6,
            9,
            10,
            12,
            16,
            17,
        ]
    }
)
data["degrees1"].value_counts().plot(
    ax=ax, kind="bar", xlabel="degrees", ylabel="frequency"
)
plt.yticks(np.arange(0, 12, step=1))
plt.show()


# 2. Screenshots of Visualizations: Kamada Kawai, Fruchterman Reingold, Circular, Random, Spectral, Spring

# Kamada Kawai
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.kamada_kawai_layout.html

plt.title("kamada_kawai")
nx.draw(
    G, with_labels=True, node_size=600, node_color="skyblue", pos=nx.kamada_kawai_layout(G)
)
plt.savefig("kamada_kawai.png")
plt.show()

# Fruchterman Reingold
plt.title("fruchterman_reingold")
nx.draw(
    G,
    with_labels=True,
    node_size=600,
    node_color="skyblue",
    pos=nx.fruchterman_reingold_layout(G),
)
plt.savefig("fruchterman_reingold.png")
plt.show()


# Circular
plt.title("circular")
nx.draw(
    G, with_labels=True, node_size=600, node_color="skyblue", pos=nx.circular_layout(G)
)
plt.savefig("circular.png")
plt.show()


# Random
plt.title("random")
nx.draw(
    G, with_labels=True, node_size=600, node_color="skyblue", pos=nx.random_layout(G)
)
plt.savefig("random.png")
plt.show()


# Spectral
plt.title("spectral")
nx.draw(
    G, with_labels=True, node_size=600, node_color="skyblue", pos=nx.spectral_layout(G)
)
plt.savefig("spectral.png")
plt.show()


# Spring
plt.title("spring")
nx.draw(
    G, with_labels=True, node_size=600, node_color="skyblue", pos=nx.spring_layout(G)
)
plt.savefig("spring.png")
plt.show()


# 3. Centralities: 4 kinds

print("Degree Centrality")
print(nx.degree_centrality(G))
print("\n")
print("Closness Centrality")
print(nx.closeness_centrality(G))
print("\n")
print("Betweeness Centrality")
print(nx.betweenness_centrality(G))
print("\n")
print("Eigenvector Centrality")
print(nx.eigenvector_centrality(G))
