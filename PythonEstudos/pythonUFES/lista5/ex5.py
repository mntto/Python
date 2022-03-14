def media_vizinhos (lista) :
    novaLista = []
    for i in range (0,len(lista)): 
        if i == 0 : 
            auxiliar = ( lista[0] + lista[1] ) / 2 
            novaLista.append(auxiliar)
        elif 0 < i < len(lista) - 1 : 
            auxiliar = ( lista[i - 1] + lista[i] + lista[i + 1] ) / 3
            novaLista.append(auxiliar)    
        else : 
            auxiliar = ( lista[i-1] + lista[i] ) / 2
            novaLista.append(auxiliar)
              
    return(novaLista) 

print(media_vizinhos([1,2,3,4,5]))

input('Fim')