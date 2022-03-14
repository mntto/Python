numeroconj = int(input("Digite a quantidade de conjuntos: ")) 

while numeroconj < 1 : 
    numeroconj = int(input("Digite a quantidade de conjuntos maior ou igual a 1: ")) 
numero1 = float(input("Digite um número qualquer: ")) 
numero2 = float(input("Digite um número qualquer maior do que o primeiro: ")) 
numero3 = float(input("Digite um número qualquer maior do que o segundo: ")) 
if numero1 < numero2  < numero3 :
    soma = numero1 + numero2 + numero3 
    produto = numero1 * numero2 * numero3
    media = (soma)/3 
    print("A soma do conjunto 1 é:", soma ) 
    print("O produto do conjunto 1 é:", produto) 
    print("A media do conjunto 1 é:", media) 
    for i in range (1,numeroconj,1) :
        while numero1 < numero2 < numero3 :   
            numero1 = float(input("Digite um número qualquer: ")) 
            numero2 = float(input("Digite um número qualquer maior do que o primeiro: ")) 
            numero3 = float(input("Digite um número qualquer maior do que o segundo: ")) 
            if numero1 < numero2 < numero3 :
                soma = numero1 + numero2 + numero3 
                produto = numero1 * numero2 * numero3
                media = (soma)/3 
                print("A soma do conjunto", i,"é:", soma ) 
                print("O produto do conjunto", i,"é:", produto) 
                print("A media do conjunto", i,"é:", media)
            if not numero1 < numero2 < numero3 :
                print("Os números não foram digitados na ordem crescente!") 
else :
    print("Os números não foram digitados na ordem crescente!")    
input("Fim")