#2 Part 2 Louvain Algorithm
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_comm

edgelist_file = 'congress.edgelist'
G = nx.read_edgelist(edgelist_file)

def set_node_community(G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1

def set_edge_community(G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0

def get_color(i, r_off=1, g_off=1, b_off=1):
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)

partition=nx_comm.louvain_communities(G, seed=123)


set_node_community(G, partition)
set_edge_community(G)

# Set community color for nodes
node_color = [get_color(G.nodes[v]['community']) for v in G.nodes]

# Set community color for internal edges
external = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] == 0]
internal = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] > 0]
internal_color = [get_color(G.edges[e]['community']) for e in internal]

pos1 = nx.spring_layout(G)
# Draw external edges
nx.draw_networkx(
    G,
    pos=pos1,
    node_size=0,
    edgelist=external,
    edge_color="#333333")
# Draw nodes and internal edges
nx.draw_networkx(
    G,
    pos=pos1,
    node_color=node_color,
    edgelist=internal,
    edge_color=internal_color)
plt.show()

#returns communities
print("# of communities: ", len(partition), ", modularity score: ", nx_comm.modularity(G, partition))