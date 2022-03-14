lista = []
elementos = int(input("Informe o número de elementos: ")) 

for i in range (0,elementos) :
    print("Digite o elemento",i,"° :")
    auxiliar = float(input())
    lista.append(auxiliar)

print("Os elementos são:",lista) 
auxiliar = int(input("Digite qual elemento você quer pocurar na lista:"))
if lista.count(auxiliar) == 0 : 
    print(-1)
else  :  
    print(lista.index(auxiliar))

input("Fim")