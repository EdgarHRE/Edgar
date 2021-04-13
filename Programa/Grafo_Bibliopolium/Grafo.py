
from Grafo_Bibliopolium.nodes import Node
from Grafo_Bibliopolium.arist import Arist

class Grafo:
    def __init__(self,new_num_nodos,new_flag_arist,new_flag):
        self.num_nodos = new_num_nodos
        self.flag_arist = new_flag_arist
        self.flag = new_flag
    
    def __repr__(self):
        return f'{self.num_nodos}'
    
    def __repr__(self):
        return f'{self.flag.arist}'
    
    def Num_Node(num_nodos):
        flag_list1 = []
        flag_list2 = []
        
        for x in range(1,num_nodos+1):
            a = f'Node {x}'
            flag_list1.append(a)
        
        for y in range(1,num_nodos+1):
            flag_list2.append(y)
            
        nodes = dict(zip(flag_list1,flag_list2))
        return nodes          
    
    def Arista(flag_arist):
        if flag_arist == 0:
            return False
        else:
            return True
    