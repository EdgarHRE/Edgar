import pygraphviz as pgv
from Grafo_Bibliopolium.Grafo import Grafo
from random import randint

    
n = int(input('Ingrese el valor de n nodos: '))
m = int(input('Ingresa el valor de m aristas: '))

Node = Grafo.Num_Node(n)
print(Node)

G = pgv.AGraph(directed= Grafo.Arista(0))

G.node_attr['shape'] = 'point'


for i in Node.values():
    G.add_node(i, color='pink')
    
    
    
list_node = []
i=1

while i <= m:     
    n1 = randint(1,n)
    n2 = randint(1,n)
    if n1 != n2:
        flag = (n1,n2)
        flag2 = (n2,n1)
        if flag not in list_node:
            G.add_edge(n1,n2)
            print(f'{n1} -> {n2}')
        else:
            i = i-1
    
    else:
        i = i-1

    list_node.append(flag)
    list_node.append(flag2)
    
    i = i +1
        
    

G.layout()
G.draw('Erdos_Renyi.png', prog='dot')
G.draw('Erdos_Renyi_500_Nodos.dot')

     
