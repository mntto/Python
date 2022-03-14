def paresImpares (bagunça) : 
    pares = []
    impares = []
    for i in bagunça : 
        if i % 2 == 0 : 
            pares.append(i)
        else : 
            impares.append(i)             
    return(pares,impares) 

print(paresImpares([1,2,3,4])) 
print(paresImpares([1,3])) 
print(paresImpares([2,4])) 