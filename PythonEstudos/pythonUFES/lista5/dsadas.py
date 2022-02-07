def media_vizinhos (lista) :
    novaLista = lista 
    for i in range (0,len(lista)): 
        if i == 0 : 
            novaLista[i] = ( lista[0] + lista[1] ) / 2 
        elif 0 < i < len(lista) - 1 : 
            print(lista[i-1],lista[i],lista[i+1])
            novaLista[i]= ( lista[i - 1] + lista[i] + lista[i + 1] ) / 3    
        else : 
            print(lista[i-1],lista[i])
            novaLista[i] = ( lista[i-1] + lista[i] ) / 2
              
    return(novaLista) 

print(media_vizinhos([1,2,3,4,5]))

input('Fim')