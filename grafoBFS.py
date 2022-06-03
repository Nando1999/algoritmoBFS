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

     # Constructor
    def __init__(self, num_Nodos, dirigido=True):
        """
        Método constructor de la clase Grafo, donde inicializa sus parámetros

        Parámetros
            ----------
            num_Nodos : int
                Número de nodos del grafo
            dirigido : boolean
                Tipo de grafo dirigido o no dirigido
        """
        # Define el número de nodos
        self.m_num_Nodos = num_Nodos
        # Define el rango del número de nodos
        self.m_Nodos = range(self.m_num_Nodos)

        # Tipo de grafo dirigido o no dirigido
        self.m_dirigido = dirigido

        # Representación de la lista de adyacencia
        # Para la implementación de la lista de adyacencia se usa un diccionario
        self.m_lista_adyacencia = {node: set() for node in self.m_Nodos}

    # Añande una arista al grafo
    def agregar_Arista(self, nodo1, nodo2, peso=1):