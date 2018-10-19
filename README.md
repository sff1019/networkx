# About
Project using networkx

# Data
Social circles: Facebook .   

Source: https://snap.stanford.edu/data/ego-Facebook.html

# Demo Code

```
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
```

# Output
## Analyzing based on community
![Community Analysis](https://raw.githubusercontent.com/sff1019/networkx/master/outputs/community_nt.png)

## Analyzing based on degree size
![Degree Analysis](https://raw.githubusercontent.com/sff1019/networkx/master/outputs/degree_nx.png)

# Reference
https://blog.dominodatalab.com/social-network-analysis-with-networkx/
