def TrocaValores (d1,d2) :
    DicTroc = {} 
    for d1key, d2val in zip (d1,d2.values()):
        DicTroc[d1key] = d2val 
    return(DicTroc)

dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}  

print(TrocaValores(dict1,dict2)) 

input('Fim')