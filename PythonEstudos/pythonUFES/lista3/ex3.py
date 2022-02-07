numero = int(input("Digite um número de 1 a 10: ")) 

while numero < 1 or numero > 10 : 
    numero = int(input("Por favor, digite um número de 1 a 10: ")) 

for i in range (1,11,1) : 
    print(numero,"*",i,"=",i*numero) 

input("Fim")