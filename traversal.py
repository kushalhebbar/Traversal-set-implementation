import networkx as nx
import matplotlib.pyplot as plt
import time
from datetime import timedelta

#Notes start time of program
start_time = time.monotonic()

#Code snippet to generate a small graph to analyze traversal set implementation
'''G=nx.Graph()
G.add_nodes_from([1,8])

G.add_edges_from([(1,2), (1,3), (3,4), (2,5),(5,6), (5,7), (7,8)])

nx.draw(G, with_labels = True)
plt.show() '''

#Generates a random graph
G=nx.Graph()

#Either of the following 2 methods can be used to generate random graphs
#G=nx.random_regular_graph(3, 10000, seed=None)
G = nx.fast_gnp_random_graph(600,0.8)

#Converts graph labels to integers
F = nx.convert_node_labels_to_integers(G, first_label=1, ordering='default', label_attribute=None)
print(F.number_of_nodes())

nx.draw(F)
plt.show()

#traversal set edge 
s=5
t=6

traversal = []
count=0
for i in range(1, F.number_of_nodes()):
    for j in range(i+1, F.number_of_nodes()+1):
        if nx.has_path(F, i, j):
            shortest_path = nx.shortest_path(F, i,j) #calculates shortest path
            if s in shortest_path and t in shortest_path:
                traversal.append([i,j])
                count+=1
print(traversal) #Prints the traversal set
print(count)

#Notes the end time of the program
end_time = time.monotonic()

#Calculates time elapsed
print(timedelta(seconds=end_time - start_time))
