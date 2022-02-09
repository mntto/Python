# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():  
    def __init__(self, nome=" ", cidade=" ", telefone=0, email=" "):
        self.nome = nome 
        self.cidade = cidade 
        self.telefone = telefone 
        self.email = email 

    def __str__(self): 
        return "Nome: %s, telefone: %s, cidade: %s, e-mail: %s"\
        %(self.nome,self.telefone,self.cidade,self.email) 

pessoa1 = Pessoa("Mylson", "Vitória", 27992919710,"mnetto00@gmail.com") 

print(str(pessoa1)) 

input("End")