# IDEA: Cell towers that are too close to one another will need to have different frequencies. Since purchasing frequencies costs money,
#       minimize the amount of frequencies needed with graph theory.

from scipy.spatial import distance_matrix
import math
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Load in the data
tower_data = open_file('TowersVNZ476413FDC428783.csv')

# Save latitude and longitude as variables
lat = tower_data['latitude']
long = tower_data['longitude']

# Plot towers
plt.figure()
plt.scatter(long, lat)
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.axis('equal')

# Possible solution for the nearest-neighbor algorithm
latar = np.array(tower_data['latitude'])
longar = np.array(tower_data['longitude'])
coord_array = np.vstack((longar, latar)).T


def distance(p1, p2):
    '''Returns the distance betwen two numpy points'''
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def nn_graph(points):
    '''Generates an adjacency matrix based on the Nearest neighbor graph algorithm.'''
    G = dict()
    for p in range(0, len(points)):
        min_distance = np.inf
        min_point = -1
        for n in range(0, len(points)):
            if p != n:
                d = distance(points[p], points[n])
                if d < min_distance:
                    min_distance = d
                    min_point = n
        if min_point == -1:
            print("ERROR-point not found")
        G[p] = min_point
    return G


# testing code here


def knn(coord_array, K):
    '''Finds the nearest K neighbors and set to dict, G.'''
    G = dict()
    dist = distance_matrix(coord_array, coord_array)  # create a distance matrix
    for value in range(len(dist)):

        # argsort will return index
        sort = np.argsort(dist[value])
        closest = sort[1:K + 1]
        G[value] = closest
    return G


'''Cell tower plot with needed coloring for frequencies'''

p = nx.Graph(knn(coord_array, 3))  # nx.Graph() contains node and edge information
# color the graph using specified coloring strategy
d = nx.greedy_color(p, strategy=nx.coloring.strategy_largest_first)
l = list(d.values())  # varaible holding node coloring information

graph = nx.draw(p, coord_array, node_size=69, cmap='tab20c', node_color=l,
                with_labels=False)
