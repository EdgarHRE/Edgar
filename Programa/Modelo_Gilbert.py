import pygraphviz as pgv
from Grafo_Bibliopolium.Grafo import Grafo
from random import random
from random import choice

list_colors = ['red', 'yellow', 'teal', 'violet', 'lime', 'cyan', 'magenta', 'orange', 'navy', 'indigo'
               'marron', 'sienna']

n = int(input('Ingrese el de valor de n nodos: '))
p = float(input('Ingrese el valor de la probabilidad p: '))

Node = Grafo.Num_Node(n)
print(Node)

G = pgv.AGraph(directed= Grafo.Arista(0))

G.node_attr['shape'] = 'point'


for i in Node.values():
    G.add_node(i, color='yellow')

  
for i in Node.values():
    for j in Node.values():
        if i != j:
            x = random()  
            if x <= p:
                G.add_edge(i,j)
                print(f'P={x}; {i} -> {j}')
            else:
                continue
            
        else:
            continue
    

G.layout()
G.draw('Gilbert.png', prog='dot')
G.draw('Gilbert_500_Nodos.dot')
