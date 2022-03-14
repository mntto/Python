soma = lambda a, b : a + b 
subtração = lambda a1, b1 : a1 + b1 
multi = lambda a2, b2 : a2 * b2 
divi = lambda a3, b3 : a3 / b3

print('calculadora py') 
continuar = "s" 
opcao = 5
while continuar == "s" : 
    while opcao < 0 or opcao > 4 :  
        opcao = int(input("Opções disponíveis:\n 1-Soma \n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n Digita a operação que deseja realizar:"))

    num1 = float(input("Digite o primeiro número : ")) 
    num2 = float(input("Digite o segundo número : "))
    if opcao == "1" : 
        num3 = soma(num1,num2)
        print(num1,"+",num2,"=",num3) 
    elif opcao == "2" : 
        num3 = subtração(num1,num2)
        print(num1,"-",num2,"=",num3) 
    elif opcao == "3" : 
        num3 = multi(num1,num2) 
        print(num1,"*",num2,"=",num3)
    else : 
        num3 = divi(num1,num2) 
        print(num1,"/",num2,"=",num3)

    continuar = input("Deseja continuar s/n :")    
         
input("Fim")