linha1_1 = [0,0,0,0] 
linha2_1 = [0,0,0,0]
linha3_1 = [0,0,0,0]
linha4_1 = [0,0,0,0]
linha1_2 = [0,0,0,0]
linha2_2 = [0,0,0,0]
linha3_2 = [0,0,0,0]
linha4_2 = [0,0,0,0]       
matriz1 = [linha1_1, linha2_1, linha3_1, linha4_1] 
matriz2 = [linha1_2, linha2_2, linha3_2, linha4_2] 
matriz3 = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]
axiliar = 0

for i in range (0,4,1) : 
    for j in range (0,4,1) :
        print("Posição a",i+1,j+1) 
        matriz1[i][j] = float(input("Digite um número para fazer parte da matriz 1: ")) 

for i in range (0,4,1) : 
    for j in range (0,4,1) :
        print("Posição a",i+1,j+1) 
        matriz2[i][j] = float(input("Digite um número para fazer parte da matriz 2: ")) 
        
print("Matriz 1 =", matriz1) 
print("Matriz 2 =", matriz2)

for i in range (0,4,1) : 
    for j in range (0,4,1) :
        if matriz2[i][j] >= matriz1[i][j] :
            matriz3 [i][j] = matriz2[i][j] 
        else : 
            matriz3 [i][j] = matriz1[i][j]

print("Matriz 3 =", matriz3)

input("Fim")