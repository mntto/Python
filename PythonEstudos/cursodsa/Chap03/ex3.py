lista = [0,0,0,0]  

def add2list (list) :
    for i in range (0,2,1) : 
        list.append(input("adicione algo a lista:")) 
    return(list) 

lista = add2list(lista)  
print(lista)

input('Fim')