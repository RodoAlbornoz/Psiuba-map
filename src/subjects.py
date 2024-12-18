import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

subjects = [
    "Materia 1", 
    "Materia 2", 
    "Materia 3", 
    "Materia 4", 
    "Materia 5"
]

edges = [
    ("Materia 1", "Materia 2"), 
    ("Materia 1", "Materia 3"), 
    ("Materia 3", "Materia 4"), 
    ("Materia 2", "Materia 5")
]

graph = nx.DiGraph()
graph.add_nodes_from(subjects)

graph.add_edges_from(edges)

nx.draw_spectral(
    graph, 
    with_labels = True, 
    node_color = 'skyblue', 
    node_size = 3500, 
    font_size = 12
)

plt.show()