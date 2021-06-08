
from lib_tools.grafo import Grafo
from lib_tools import Modelo_Barabasi, Modelo_Malla
from lib_tools import Modelo_Erdos_Rengy
from lib_tools import Modelo_Gilbert
from lib_tools import Modelo_Geo_S
from lib_tools import Modelo_Dorogo_M
from lib_tools import Modelo_Barabasi


print('Bienvenido...')
print('El siguiente programa es un Menu de modelo de Grafos.')
print('Ingresa la opcion 1 si deseas crear un Grafo tipo Malla')
print('Ingresa la opcion 2 si deseas crear un Grafo tipo Erdos_Rengi')
print('Ingresa la opcion 3 si deseas crear un Grafo tipo Gilbert')
print('Ingresa la opcion 4 si deseas crear un Grafo tipo Geo_SImple')
print('Ingresa la opcion 5 si deseas crear un Grafo tipo Dorogovtsev-Mendes')
print('Ingresa la opcion 6 si deseas crear un Grafo tipo Barabasi')


x = 'si'


while x == 'si':
    
    op = int(input('Cual es la opcion que deseas: '))
    
    if op == 1:
        print('Elegiste el Grafo de Malla.')
        m = int(input('Ingresar el valor de m nodos de la malla: '))
        n = int(input('Ingresar el valor de n nodos de la malla: '))
        GRAFO = Modelo_Malla.Malla(m,n)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
    
    elif op == 2:
        print('Elegiste el Grafo de Erdos_Rengi')
        n = int(input('Ingrese el valor de n nodos: '))
        m = int(input('Ingresa el valor de m aristas: '))
        GRAFO = Modelo_Erdos_Rengy.Erdos_Renyi(n, m, directed = False, auto = False)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
    
    elif op == 3:
        print('Elegiste el Grafo de Gilbert')
        n = int(input('Ingrese el valor de n nodos: '))
        p = float(input('Ingresa el valor de la probabilidad p: '))
        GRAFO = Modelo_Gilbert.Gilbert(n,p, directed= False, auto = False)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
    
    elif op == 4:
        print('Elegiste el Grafo de Geografico Simple')
        n = int(input('Ingrese el valor de n nodos: '))
        r = float(input('Ingresa la distancia r: '))
        GRAFO = Modelo_Geo_S.Geo_S(n, r, directed= False, auto = False)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
    
    elif op == 5:
        print('Elegiste el Grafo de Dorogovtsev-Mendes')
        n = int(input('Ingrese el valor de n nodos: '))
        GRAFO = Modelo_Dorogo_M.Dorogo_M(n, directed= False)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
    
    elif op == 6:
        print('Elegiste el Grafo de Barabasi')
        n = int(input('Ingrese el valor de n nodos: '))
        d = int(input('Ingresa el valor de  d: '))
        GRAFO = Modelo_Barabasi.Barabasi(n,d,directed=False, auto=False)
        n_archivo = str(input('Ingresa el nombre del archivo: '))
        dot = GRAFO.graphiv(n_archivo)
           
    
    x = str(input('Deseas continuar (si), Salir... (salir): '))
 