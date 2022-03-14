def triangulo (X, Y, Z) :
    tipoTri = ""
    if X < Y + Z and Y < X + Z and Z < X + Y : 
        if X == Y == Z :
            tipoTri = "Triângulo Equilátero"
        elif X == Y or Y == Z or X == Z :
            tipoTri = "Triângulo Isósceles"
        else : 
            tipoTri = "Triângulo Escaleno"
    else: 
        tipoTri = "Não pode ser um triângulo" 
    return(tipoTri)  

num1 = float(input("Digite o primeiro lado do triângulo: ")) 
num2 = float(input("Digite o segundo lado do triângulo: "))
num3 = float(input("Digite o terceiro lado do triângulo: "))  

print("O trianguldo formado por (",num1,",",num2,",",num3,") :") 

print(triangulo(num1,num2,num3)) 

input('Fim')