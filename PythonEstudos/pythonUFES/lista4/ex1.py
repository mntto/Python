lista = [] 
auxiliar = 0  

for i in range (0,10,1) :
    auxiliar = float(input("Digite um número para entrar para sua lista: " ))
    if auxiliar > 0 : 
        lista.append(auxiliar)  
    else : 
        lista.append(0)
      
print(lista) 
input("Fim")