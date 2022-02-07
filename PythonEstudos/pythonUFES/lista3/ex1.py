numero = float(input("Digite um número :"))
maiornumero = float(input("Digite um outro número :"))
menornumero = float(input("Digite um outro número :"))  
auxiliar = float 

if numero > maiornumero or menornumero > maiornumero : 
    if numero > menornumero :  
        if maiornumero < menornumero : 
            menornumero = maiornumero
            maiornumero = numero 
        else : 
            maiornumero = numero    
    else :  
        if numero < maiornumero :
            auxiliar = numero  
            maiornumero = menornumero 
            menornumero = auxiliar 
        else : 
            auxiliar = maiornumero 
            maiornumero = menornumero 
            menornumero = auxiliar
elif maiornumero > numero and maiornumero > menornumero : 
    if numero < menornumero : 
        menornumero = numero      

for i in range (0,7,1) :  
    auxiliar = float(input("Digite um outro número: "))
    if maiornumero < auxiliar : 
        maiornumero = auxiliar 
    elif menornumero > auxiliar : 
        menornumero = auxiliar 
    
print("\nO maior número é :",maiornumero,"\n","O menor número é:",menornumero) 

input("Fim")