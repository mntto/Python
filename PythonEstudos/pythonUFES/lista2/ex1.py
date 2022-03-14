mês = int(input("Digite um número de 1 a 12, para saber o nome do mês correspondete: ")) 

if mês >= 1 and mês <= 12 : 
    if mês == 1: 
        print(mês, "Corresponde ao mês de Janeiro!")
    elif mês == 2: 
        print(mês, "Corresponde ao mês de Fevereiro!")
    elif mês == 3: 
        print(mês, "Corresponde ao mês de Março!")
    elif mês == 4: 
        print(mês, "Corresponde ao mês de Abril!")
    elif mês == 5: 
        print(mês," Corresponde ao mês de Maio!")
    elif mês == 6: 
        print(mês, "Corresponde ao mês de Junho!")
    elif mês == 7: 
        print(mês, "Corresponde ao mês de Julho!")
    elif mês == 8: 
        print(mês, "Corresponde ao mês de Agosto!")
    elif mês == 9: 
        print(mês, "Corresponde ao mês de Setembro!")
    elif mês == 10: 
        print(mês, "Corresponde ao mês de Outubro!")
    elif mês == 11: 
        print(mês, "Corresponde ao mês de Novembro!")
    else : 
        print(mês, "Corresponde ao mês de Dezembro!")
else : 
    print("digite um numero correspondente.") 

input("Fim") 
