
print("Escolha o número de uma das opções a baixo:\n 1 - Soma de dois números.\n 2 - Diferença entre dois números(maior pelo menor).\n 3 - Produto entre dois números.\n 4 - Divisão entre dois números(o denominador não pode ser zero).\n  ")
opção = int(input("Digite a opção escolhida: ")) 
if opção == 1 or opção == 2 or opção == 3 or opção == 4 : 
    A = float(input("Digite um número qualquer: "))
    B = float(input("Digite um outro número qualquer: "))
    if opção == 1 : 
       print( A + B ) 
    elif opção == 2 :
        if A > B: 
            print(A - B)
        else : 
            print(B - A)
    elif opção == 3: 
        print(A*B)
    else :
        if A == 0 : 
            print(A/B)
        elif B == 0: 
            print(B/A) 
        else : 
            print(A/B)
else : 
    print("Digite uma opção valida.") 



input("Fim")