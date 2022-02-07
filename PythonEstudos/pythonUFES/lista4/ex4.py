linha1 = [0,0,0,0,0]
linha2 = [0,0,0,0,0] 
linha3 = [0,0,0,0,0]
linha4 = [0,0,0,0,0]
linha5 = [0,0,0,0,0] 
matriz1 = [linha1, linha2, linha3, linha4, linha5] 

for i in range (0,5,1) : 
    for j in range (0,5,1) :
        print("Posição a",i+1,j+1) 
        matriz1[i][j] = float(input("Digite um número para fazer parte da matriz 1: ")) 

print("A matriz é dada por :",matriz1)
 
a = matriz1[0][1] + matriz1[0][2] + matriz1[0][3] + matriz1[0][4] + matriz1[1][2] + matriz1[1][3] + matriz1[1][4] + matriz1[2][3] + matriz1[2][4] + matriz1[3][4] 
print("Soma dos elemento acima da diagonal principal: ", a) 

b = matriz1[1][0] + matriz1[2][0] + matriz1[2][1] + matriz1[3][0] + matriz1[3][1] + matriz1[3][2] + matriz1[4][0] + matriz1[4][1] + matriz1[4][2] + matriz1[4][3] 
print("Soma dos elemento abaixo da diagonal principal: ", b) 

c =  matriz1[0][0] + matriz1[1][1] + matriz1[2][2] +  matriz1[3][3] + matriz1[4][4] 
print("A soma dos elementos da diagonal principal é:", c) 

d =  matriz1[0][4] + matriz1[1][3] + matriz1[2][2] + matriz1[3][1] + matriz1[4][0] 
print("A soma dos elementos da diagonal secundária é:", d) 

input("Fim")