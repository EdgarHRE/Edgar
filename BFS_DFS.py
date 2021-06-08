
from lib_tools import Modelo_G_Aleatorio


print('Bienvenido')
print('El siguiente programa es un menu para la obtencion de algoritmos BFS y DFS')
print('Ingresa la opcion 1 si deseas usar el Algoritmo BFS.')
print('Ingresa la opcion 2 si deseas usar el Algoritmo DFS.')
print('Ingresa la opcion 3 si deseas usar el Algoritmo DFS-Recursivo')

x = 'si'


while x == 'si':
    
    op = int(input('Cual es la opcion que deseas: '))
    
    if op == 1:
        
        print('Elegiste usar el Algorimo BFS.')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        print('Se Genera un Grafo Aleatorio, donde se crearan m nodos que ingresaste')
        print('Y las aristas se crearan aleatoriamente de acuerdo a la funcion randint()')
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
        n_raiz = int(input('Ingrese el nodo raiz que desea usar para el Algortimo BFS: '))
        GRAF = GRAFO.BFS(n_raiz)
        n_archivo2 = str(input('Ingrese el nombre del archivo: '))
        dot = GRAF.graphiv(n_archivo2) 
    
    elif op == 2:
        print('Elegiste usar el Algorimo DFS.')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
        n_raiz = int(input('Ingrese el nodo raiz que desea usar para el Algortimo DFS: '))
        GRAF = GRAFO.DFS(n_raiz)
        n_archivo2 = str(input('Ingrese el nombre del archivo: '))
        dot = GRAF.graphiv(n_archivo2)
    
    elif op == 3:
        print('Elegiste usar el Algoritmo DFS-Recursivo')
        m = int(input('Ingresar el valor de m nodos del Grafo Aleatorio: '))
        GRAFO = Modelo_G_Aleatorio.Grafo_A(m)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
        n_raiz = int(input('Ingrese el nodo raiz que desea usar para el Algoritmo DFS-Recursivo: '))
        GRAF = GRAFO.DFS_R(n_raiz)
        n_archivo2 = str(input('Ingresa el nombre del archivo: '))
        dot = GRAF.graphiv(n_archivo2)
    
    x = str(input('Deseas continuar (si), Salir... (salir): '))
 