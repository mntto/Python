planeta = str(input("Digite o nome ou o número do planetas onde você deseja calcular o seu peso:\n 1 - Mercúrio\n 2 - Vênus\n 3 - Marte\n 4 - Júpiter\n 5 - Saturno\n 6 - Urano\n Escolha o planeta: \n" ))    
peso = float(input("Digite seu peso em Kg: "))
 
if planeta == "1" or planeta == "Mercúrio" : 
    peso = peso * 0.37
    print("Seu peso em Mercúrio é: ",peso ,"Kg") 
elif planeta == "2" or planeta == "Vênus" :
    peso = peso * 0.88
    print("Seu peso em Vênus é: ",peso ,"Kg")
elif planeta == "3" or planeta == "Marte" :
    peso = peso * 0.38
    print("Seu peso em Marte é: ",peso ,"Kg")
elif planeta == "4" or planeta == "Júpiter" :
    peso = peso * 2.64
    print("Seu peso em Júpiter é: ",peso ,"Kg")
elif planeta == "5" or planeta == "Saturno" :
    peso = peso * 1.15
    print("Seu peso em Saturno é: ",peso ,"Kg")
elif planeta == "6" or planeta == "Urano" :
    peso = peso * 1.17
    print("Seu peso em Uranp é: ",peso ,"Kg")
else : 
    print("Digite um nome ou um número referente a um plante.")


input("Fim")