from BFS_DFS import GRAFO
import collections
from lib_tools.Modelo_G_Aleatorio import Grafo_A

from graphviz import Digraph
from graphviz import Graph as Graphviz
from lib_tools import aristas
from lib_tools import nodos

# Attribute to indicate if is a directed graph
DIRECTED = "DIRECTED"
RENDER = False
DISCOVERED = "DISCOVERED"


class Grafo:
    def __init__(self, num_nodos=None, num_aristas=None, atrbt={}):
        
        if num_nodos is None:
            num_nodos = {}
        self.num_nodos = num_nodos
        
        if num_aristas is None:
            num_aristas = {}
        self.num_aristas = num_aristas
        
        self.atrbt = atrbt
        
    def Aristas_Aleatorias(self):
        aristas = []
        for (key, value) in self.num_aristas.keys():
            aristas.append((key, value))
            return aristas
    
    
    def BFS(self, s):
        GRAFO_bfs = Grafo(atrbt={DIRECTED: True})
        nodo_seleccionado = self.ID(s)
        nodo_seleccionado.atributos[DISCOVERED] = True
        q = collections.deque()
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        GRAFO_bfs.Producir_Vertices(nodo_seleccionado)
        q.append(s)
        while (len(q) > 0):
            nodo = q.popleft()
            for arista in self.Trayectoria_Adyacente(nodo, t_adyacente):
                conexion = self.ID(arista)
                if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
                    conexion.atributos[DISCOVERED] = True
                    GRAFO_bfs.append(conexion.id)
                    GRAFO_bfs.Producir_Vertices(conexion)
                    GRAFO_bfs.Producir_Aristas(aristas.Arista(nodo, arista), True)
        
        return GRAFO_bfs
    
    def DFS(self, root):
        GRAFO_dfs = Grafo(atrbt={DIRECTED: True})
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        pila = collections.deque()
        pila.append(('#', root))
        while (len(pila) > 0):
            (origen, destino) = pila.pop()
            conexion = self.ID(destino)
            if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
                conexion.atributos[DISCOVERED] = True
                GRAFO_dfs.Producir_Vertices(conexion)            
                if (origen != '#'):
                    GRAFO_dfs.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
                for arista in self.Trayectoria_Adyacente(conexion.id,t_adyacente):
                    pila.append((conexion.id, arista))
        
        return GRAFO_dfs 
    
    def DFS_R(self, root):
        GRAFO_dfsr = Grafo(atrbt={DIRECTED: True})
        return self.Recursividad(GRAFO_dfsr, ('#', root))      
    
    def graphiv(self, n_archivo, atri_nodo = None, source = None, atri_arista = None):
        dot = Graphviz()
        
        # Review attribute directed of graph
        if DIRECTED in self.atrbt:
            if self.atrbt[DIRECTED]:
                dot = Digraph()
            else:
                dot = Graphviz()
        
        if atri_nodo is None:
            for n in list(self.num_nodos.keys()):
                dot.node(str(n), str(n))        
        else:
        # Map graph to graphviz structure and add vertex attribute
            for n in list(self.num_nodos.keys()):
                label = "Nodo: " + str(n)
                source_label = "Nodo source: " + str(source) if source is not None else ""
                label = label + "\n" + source_label
                label = label + "\n" + atri_nodo + " (" + str(self.num_nodos[n].atributos[atri_nodo]) + ")"
                dot.node(str(n), label)
        
        if atri_arista is None:
            for a in self.Aristas_Aleatorias():
                (s,t) = a
                dot.edge(str(s), str(t))
        else:
            for a in self.Aristas_Aleatorias():
                (s,t) = a
                flag_arista = self.num_arista[(s,t)].atrbt["WEIGHT"]
                dot.edge(str(s), str(t), label=str(flag_arista))
                
        file = open("/home/dreadscythe/ED/Programas/Proyecto1/archivos_gv/" + n_archivo + ".gv", "w")
        file.write(dot.source)
        file.close()
        return dot
    
    def ID(self, id):
        if id in self.num_nodos.keys():
            return self.num_nodos[id]
        else:
            return None
        
    def Producir_Aristas(self, arista, directed=False, auto=False):    
        
        (nodo_a, nodo_b) = arista.P2P()
        if nodo_a in self.num_nodos.keys() and nodo_b in self.num_nodos.keys():
            if directed:
                if auto:
                    self.num_aristas[arista.P2P()] = arista
                else:
                    if nodo_a != nodo_b:
                        self.num_aristas[arista.P2P()] = arista
            else:
                if self.num_aristas.get((nodo_b, nodo_a)) is None:
                    if auto:
                        self.num_aristas[arista.P2P()] = arista
                    else:
                        if nodo_a != nodo_b:
                            self.num_aristas[arista.P2P()] = arista
    
    
    def Producir_Vertices(self,v):
        if v.id not in self.num_nodos.keys():
            self.num_nodos[v.id] = v
    
    
    
    def Recursividad(self, GRAFO_dfsr, root):
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        (origen, destino) = root
        conexion = self.ID(destino)
        if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
            conexion.atributos[DISCOVERED] = True
            GRAFO_dfsr.Producir_Vertices(conexion)
            if (origen != '#'):
                GRAFO_dfsr.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
            
            for arista in self.Trayectoria_Adyacente(conexion.id, t_adyacente):
                self.Recursividad(GRAFO_dfsr, (conexion.id, arista))
        
        return GRAFO_dfsr   
    
    def Trayectoria_Adyacente(self, id, type=None):
        nodos = []
        for (inicio, arribo) in self.num_aristas.keys():
            if type is None:
                if inicio == id:
                    nodos.append(arribo)
                elif arribo == id:
                    nodos.append(inicio)
            elif type == '+':
                if inicio == id:
                    nodos.append(arribo)
            elif type == '-':
                if arribo == id:
                    nodos.append(inicio)
        return nodos
    
    def Trayectoria_Normal(self, id, type =0):
        aristas = []
        for (inicio, arribo) in self.num_aristas.keys():
            if type == 1:
                if inicio == id:
                    aristas.append((inicio, arribo))
            elif type == 2:
                if arribo == id:
                    aristas.append((inicio, arribo))
            else:
                if inicio == id or arribo == id:
                    aristas.append((inicio, arribo))
        
        return aristas


    
    def Recursividad(self, GRAFO_dfsr, root):
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        (origen, destino) = root
        conexion = self.ID(destino)
        if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
            conexion.atributos[DISCOVERED] = True
            GRAFO_dfsr.Producir_Vertices(conexion)
            if (origen != '#'):
                GRAFO_dfsr.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
                
            for arista in self.Trayectoria_Adyacente(conexion.id, t_adyacente):
                self.Recursividad(GRAFO_dfsr, (conexion.id, arista))
        
        return GRAFO    
    
