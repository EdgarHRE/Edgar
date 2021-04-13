import pygraphviz as pgv
from Grafo_Bibliopolium.Grafo import Grafo


var_m = int(input('Ingresar el valor de m nodos de la malla: '))
var_n = int(input('Ingresar el valor de n nodos de la malla: '))

nodos_totales = var_m * var_n

Node = Grafo.Num_Node(nodos_totales)
print(Node)

flag = []

for i in range(1,var_m+1):
    i = i*var_m
    flag.append(i)
    

G = pgv.AGraph(directed= Grafo.Arista(0))
               
G.node_attr['shape'] = 'point'


    
for i in Node.values():
    G.add_node(i, color='green')

for i in Node.values():
    for j in Node.values():
        if i !=j:
            if (j-i) == 1:
                if i in flag:
                    continue
                else:
                    G.add_edge(i,j)
                    print(f'{i},{j}')
                    
            elif (j-i) == var_m:
                G.add_edge(i,j)
                print(f'{i}->{j}')
                   
        else: 
            continue
                    
       

G.layout()
G.draw('Malla.png', prog='dot')
G.draw('Malla_500_nodos.dot')










