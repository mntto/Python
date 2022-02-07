def quadrado (x) : 
    return(x**2) 
def cubo (y) : 
    return(y**3) 

lista = [0, 1, 2, 3, 4]  
lista1 = list(map(lambda n: [quadrado(n), cubo(n)], lista)) 
print(lista1)