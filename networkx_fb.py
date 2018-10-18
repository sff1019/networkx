import networkx as nx
import matplotlib.pyplot as plt
import community


# Import file
g = nx.read_edgelist(
        'facebook_combined.txt',
        create_using=nx.Graph(),
        nodetype=int
        )

# Print the details of the dataset
print(nx.info(g))
print(nx.betweenness_centrality(g))
print(nx.average_shortest_path_length(g))
print(sorted(nx.degree_centrality(g).values()))

# layout
spring_pos = nx.spring_layout(g)

# Detect the community using the community module
parts = community.best_partition(g)
values = [parts.get(node) for node in g.nodes()]

# Draw the 'community' graph
fig, ax = plt.subplots(figsize=(80, 80))
nx.draw_networkx(
        g,
        pos=spring_pos,
        cmap=plt.get_cmap("gist_ncar"),
        node_color=values,
        node_size=35,
        with_labels=False
        )

# If to save, uncomment the line below
# plt.savefig("community.png", format="PNG")

plt.show()
# Close once done

# Get the pagerank
pr = nx.degree_centrality(g)
plt.axis('off')
#
# # Draw the 'pagerank' graph
# # The nodes' sizes are based on the pagerank
fig, ax = plt.subplots(figsize=(80, 80))
nx.draw_networkx(
        g,
        pos=spring_pos,
        cmap=plt.get_cmap("gist_ncar"),
        node_color=list(pr.values()),
        node_size=[5000*v for v in pr.values()],
        with_labels=False
        )
# plt.savefig("Graph.png", format="PNG")
plt.show()
