linha1 = [0,0,0]
linha2 = [0,0,0] 
linha3 = [0,0,0] 
matriz = [linha1, linha2, linha3] 
auxiliar = 0
b = 1 
a = 0 ; d= 0 ; e = 0 ; e1 = 0 ; e2 = 0

for i in range (0,3,1) : 
    for j in range (0,3,1) :
        print("Posição a",i+1,j+1) 
        matriz[i][j] = float(input("Digite um número para fazer parte da matriz : ")) 
print(matriz)

for i in range (0,3,1) : 
    for j in range (0,3,1) :
        a += matriz[i][j]  
print("O somatório de todos os elmentos da matriz é:",a) 

for i in range (0,3,1) : 
    for j in range (0,3,1) : 
        b *= matriz[i][j] 
print("O produto de todos os elementos da matriz é:",b) 

for i in range (0,3,1) : 
    for j in range (0,3,1) : 
        if matriz[i][j] >= auxiliar : 
            auxiliar = matriz[i][j]
            c = matriz[i][j] 
        else : 
            c = auxiliar 
for i in range (0,3,1) : 
    for j in range (0,3,1) :
        if matriz[i][j] <= auxiliar : 
            auxiliar = matriz[i][j]
            c2 = matriz[i][j] 
        else : 
            c2 = auxiliar
print("O maior número é ",c,"o menor número é",c2) 

for i in range (0,3,1) : 
    for j in range (0,3,1) : 
        if matriz[i][j] >= 0 : 
            d += 1  
print("A quantidade de elementos não negativos da matriz é:",d) 

for i in range (0,3,1) : 
    for j in range (0,3,1) :  
        if matriz[i][j] > 0 :
            e += 1 
        elif matriz[i][j] < 0 : 
            e1 += 1
        else : 
            e2 += 1

print("A quantidade de elementos positivos da matriz é :",e) 
print("A quantidade de elementos negativos da matriz é :",e1) 
print("A quantidade de elementos neutros da matriz é :",e2) 

input("Fim")