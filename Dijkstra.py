from random import randint
from lib_tools import Modelo_G_Aleatorio


print('Bienvenido')
print('El siguiente programa para la obtencion del Algoritmo Dijikstra')

x = 'si'

while x == 'si':
    m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
    print('Se Genera un Grafo Aleatorio, donde se crearan m nodos que ingresaste')
    print('Y las aristas se crearan aleatoriamente de acuerdo a la funcion randint()')
    GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
    
    for aristas in GRAFO.num_aristas.values():
        aristas.atrbt["WEIGHT"] = randint(1,50)
    
    n_archivo = str(input('Ingresa el nombre del archivo: '))
    
    dot = GRAFO.graphiv(n_archivo, atri_arista = "WEIGHT")
    #dot.render(n_archivo, view = True)
    
    usuario = 'si'
    
    while usuario == 'si':
        nodo_inicio = int(input('Ingrese el nodo inicial del grafo para aplicar la funcion Dijkstra: '))
        nodo_final = (int(input('Ingrese el nodo final: ')))
        Djstr = GRAFO.Dijkstra(nodo_inicio, nodo_final)
        n_archivo2 = str(input('Ingrese el nombre del archivo del grafo calculado por el metodo de Dijstra: '))
        dot = Djstr.graphiv(n_archivo2, "WEIGHT", nodo_inicio)
        dot.render(n_archivo2, view = True)
        usuario = str(input('Deseas volver a  usar el algoritmo Dijkstra() escribe si o no: '))
    
    x = str(input('Deseas continuar (si), Salir... (salir): ')) 

