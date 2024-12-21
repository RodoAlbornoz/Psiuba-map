import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import json

with open('../carreras/lic_psicologia/materias.json', 'r') as file:
    materias = json.load(file)

grafo = nx.Graph()
grafo.add_nodes_from(materias)

nx.draw_spectral(
    grafo, 
    with_labels = True, 
    node_color = 'skyblue', 
    node_size = 3500, 
    font_size = 12
)

plt.show()