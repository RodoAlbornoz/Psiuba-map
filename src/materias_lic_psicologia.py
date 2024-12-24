import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import json

def obtener_materias(ruta):
    with open(ruta, 'r') as materias_json:
        materias = json.load(materias_json)

    materias

def obtener_correlativas(ruta):
    with open(ruta, 'r') as correlativas_json:
        correlativas = json.load(correlativas_json)

    correlativas 
        
def obtener_materias_cbc(materias):
    return {
        materia['materia']: {
            'carga_horaria': materia['carga_horaria_semanal']
        } for materia in materias['cbc']
    }

def obtener_materias_ciclo_general(materias):
    return {
        materia['materia']: {
            'codigos': materia['codigos'],
            'duracion': materia['duracion'],
            'carga_horaria': materia['carga_horaria_semanal']
        } for materia in materias['ciclo_formacion_general']
    }

def obtener_materias_requisito_idioma(materias):
    return {
        materia['materia']: {
            'duracion': materia['duracion'],
            'carga_horaria': materia['carga_horaria_semanal']
        } for materia in materias['requisito_idioma']
    }

def obtener_materias_ciclo_profesional(materias):
    return {
        materia['materia']: {
            'codigos': materia.get('codigos', []),  
            'duracion': materia['duracion'],
            'carga_horaria': materia['carga_horaria_semanal']
        } for materia in materias['ciclo_formacion_profesional']
    }

grafo = nx.Graph()
grafo.add_nodes_from()

nx.draw(
    grafo, 
    with_labels = True, 
    node_color = 'skyblue', 
    node_size = 3500, 
    font_size = 12
)

plt.show()