import networkx as nx
import matplotlib.pyplot as plt


# Import file
g = nx.read_edgelist(
        'facebook_combined.txt',
        create_using=nx.Graph(),
        nodetype=int
        )


nx.draw_networkx(g)
plt.show(g)
