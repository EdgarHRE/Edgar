from random import randint
from lib_tools import Modelo_G_Aleatorio

print('Bienvenido...')
print('rEl siguiente programa es un Menu para la obtencion de los 3 goritmos.')
print('rKruskal, Kruskade Prim ')
print('Ingresa la opcion 1 si tu opcion es usar el Algoritmo Kruskal')
print('Ingresa la opcion 2 si tu opcion es usar  el Algoritmo Kruskal Inverso')
print('Ingresa la opcion 3 si tu opcion es usar  el Algoritmo de Prim ')

x = 'si'

while x == 'si':
    
    op = int(input('Cual es la opcion que deseas: '))
    
    if op == 1:
        
        print('Elegiste usar el Algoritmo Kruskal')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        print('Se Genera un Grafo Aleatorio, donde se crearan m nodos que ingresaste')
        print('Y las aristas se crearan aleatoriamente de acuerdo a la funcion randint()')
        
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        for aristas in GRAFO.num_aristas.values():
            aristas.atrbt["WEIGHT"] = randint(1,50)
        
        n_archivo = str(input('Ingrese el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo, atri_arista = "WEIGHT")
        KRUSKAL = GRAFO.Kruskal()
        n_archivo2 = str(input('Ingrese el nombre del archivo del grafo calculado por el metodo de Kruskal: '))
        nodo = int(input('Ingrese el nodo principal del grafo: '))
        dot = KRUSKAL.graphiv(n_archivo2, atri_arista = "WEIGHT", source = nodo)
    
    if op == 2:
        print('Elegiste usar el Algoritmo Kruskal Inverso')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        print('Se Genera un Grafo Aleatorio, donde se crearan m nodos que ingresaste')
        print('Y las aristas se crearan aleatoriamente de acuerdo a la funcion randint()')
        
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        for aristas in GRAFO.num_aristas.values():
            aristas.atrbt["WEIGHT"] = randint(1,50)
        
        n_archivo = str(input('Ingrese el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo, atri_arista = "WEIGHT")
        #dot.render(n_archivo, view = True)
        R_KRUSKAL = GRAFO.Reverso_Kruskal()
        n_archivo2 = str(input('Ingrese el nombre del archivo del grafo calculado por el metodo de Kruskal: '))
        dot = R_KRUSKAL.graphiv(n_archivo2, atri_arista = "WEIGHT", source = 0)
    
    if op == 3:
        print('Elegiste usar el Algoritmo Prim')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        print('Se Genera un Grafo Aleatorio, donde se crearan m nodos que ingresaste')
        print('Y las aristas se crearan aleatoriamente de acuerdo a la funcion randint()')
        
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        for aristas in GRAFO.num_aristas.values():
            aristas.atrbt["WEIGHT"] = randint(1,50)
        
        n_archivo = str(input('Ingrese el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo, atri_arista = "WEIGHT")
        PRIM = GRAFO.Prim()
        n_archivo2 = str(input('Ingrese el nombre del archivo del grafo calculado por el metodo de Prim: '))
        dot = PRIM.graphiv(n_archivo2, atri_arista = "WEIGHT", source = 124) 
        
    
    x = str(input('Deseas continuar (si), Salir... (salir): '))