def somatorio (numero) :
    numero = int(numero)
    while numero < 0 :
        numero = int(input("Digite um número inteiro positivo: "))
    soma = 0  
    for i in range (1,numero + 1) :
        soma += 1/i  
    return(soma) 

print(somatorio(10000)) 
print(somatorio(-1))