palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()     
lista = list(map(lambda w: [w.upper() ,w.lower(),len(w)],palavras)) 
print(lista)