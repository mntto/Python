sexo = str(input("Digite se você é Homem ou Mulher: ")) 
altura = float(input("Digite a sua altura em metros: ")) 
peso =  float(input("Digite o seu peso em Kg: ")) 

if sexo == "Mulher" : 
    pideal = (62,1 * altura) - 44,7
    pideal = "%.2f" % pideal  
    print(pideal)
    print("O seu peso ideal é de :",pideal,"Kg")
elif sexo == "Homem" :
    pideal = (72.7 * altura) - 58
    pideal = "%.2f" % pideal  
    print(pideal)
    print("O seu peso ideal é de :",pideal,"Kg")
else : 
    print("Digite Homem ou Mulher.")
    


input("Fim")