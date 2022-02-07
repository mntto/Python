continuar = "sim"   
auxiliar = 0 
#OBS.:consideirei os negativos primos, pois em todos os lugares q eu pesquisei a maioria concordavam com isso
while continuar == "sim": 
    numero = int(input("Digite o número a ser verificado diferente de 0: "))
    while numero == 0 : 
        numero = int(input("Digite um número diferente de 0: "))
    if numero > 0 : 
        passo = 1 
    else : 
        passo = -1
    for i in range (passo,numero + passo,passo) : 
        primo = numero%i 
        if primo == 0 :
            print("O número",numero,"é divisivel por",i)
            auxiliar = auxiliar + i 
    if numero == 1: 
        print("O número 1 não é primo")
    elif numero > 0 : 
        if auxiliar > (numero + 1) :
            print("O número não é primo") 
        else :
            print("O número",numero,"também é divisivel por",-1)
            print("O número",numero,"também é divisivel por",numero*-1)
            print("O numero é primo ")  
    else : 
        if auxiliar < (numero - 1) :
            print("O número não é primo") 
        else :
            print("O número",numero,"também é divisivel por",1)
            print("O número",numero,"também é divisivel por",numero*-1)
            print("O numero é primo ")
    print("Gostaria de verificar outro número ") 
    continuar = str(input("Digite sim ou não: "))

input("Fim")    