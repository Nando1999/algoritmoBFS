# Importar librería Queue
from queue import Queue

#Clase grafo en 
class Grafo:
    """
    Clase donde se realiza para representación de un Grafo
    ...
    Atributos
    ----------
    num_Nodos : int
        especifica el número de nodos del grafo a realizar 
    dirigido : boolean
        se especifica el tipo de grafo dirigido o no dirigido

    Métodos
    -------
    Se especifica los metodos a utilizar 

    __init__(numNodos, dirigido=True):
         constructor de clase grafo y los atributos 

    agrega_arista(nodo1, nodo2, peso=1):
        se añade la arista a los nodos para finalizar agregando el peso de una arista a los nodos y agrega el peso 

    imprime_ListaAdj():
        Impresión del gráfo

    busqueda_por_Amplitud(nodo_Inicio):
        Primera búsqueda por amplitud o anchura
    """