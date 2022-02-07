a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8] 
lista = list(filter(lambda x : x in a,b)) 
print(lista)