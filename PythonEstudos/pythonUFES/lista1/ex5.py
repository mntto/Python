seg = int(input("Digite a quantidade de segundos a ser convertida: "))
min = seg/60 
resto = min%60
hor = min/60 
minuto = hor%60
print(int(hor),"h :", int(minuto),"min :",int(resto),"s")