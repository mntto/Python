A = float(input("Digite um número qualquer: ")) 
B = float(input("Digite um número qualquer diferente do anterior: ")) 
C = float(input("Digite um número qualquer diferente dos 2 anteriores: ")) 

if A != B and A != B and B != C : 
    if A > B and A > C : 
        print(A) 
        if B > C: 
            print(B)
            print(C)
        else : 
            print(C)
            print(B)
    elif B > A and B > C: 
        print(B)
        if A > C : 
            print(A)
            print(C)
        else : 
            print(C)
            print(A)
    else  :
        print(C) 
        if A > B : 
            print(A) 
            print(B)
        else : 
            print(B)
            print(A)
else  : 
    print("Preencha com números diferentes!") 


input("Fim")