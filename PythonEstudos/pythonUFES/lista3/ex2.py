numero = int(input("Digite um número maior do que 0: ")) 
somapar = 0   
somaimpar = 0

while numero < 1 : 
            numero = int(input("Por favor, digite um número maior do que 0: "))

while numero < 1000 : 
    if numero % 2 == 0 :
        somapar = somapar + numero 
    else : 
        somaimpar = somaimpar + numero  
    numero = int(input("Digite um outro número maior do que 0: ")) 
    while numero < 1 : 
        numero = int(input("Por favor, digite um número maior do que 0: "))

print("\nO somatorio de números pares é: ",somapar,"\n","O somatorio de números impares é :",somaimpar) 

input("Fim")