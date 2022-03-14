A = [] 
B = [] 
C = []
auxiliar = 0 

for i in range (0,10,1) : 
    auxiliar = int(input("Digite um número para entrar na lista A : " ))
    while auxiliar <= 0 :
         auxiliar = int(input("Digite um número positivo para entrar na lista A : " ))
    A.append(auxiliar)
for i in range (0,10,1) : 
    auxiliar = int(input("Digite um número para entrar na lista B : " ))
    while auxiliar > 0 :
         auxiliar = int(input("Digite um número negativo para entrar na lista B : " ))
    B.append(auxiliar)  

print("O vetor A é dado por :",A) 
print("O vetor B é dado por :", B) 

for i in range (0,10,1) : 
    C.append( A[i] - B[i] )
    
print("O vetor A - B é :", C)

input("Fim")