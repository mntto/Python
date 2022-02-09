# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone. 
class Smartphone():
    def __init__ (self, tamanho = "Pequeno", interface = "Grande"): 
        self.tamanho = tamanho 
        self.interface = interface  
    
class MP3player(Smartphone): 
    def __init__ (self,capacidade = 0): 
        Smartphone.__init__(self) 
        self.capacidade = capacidade 
    def __str__ (self): 
        return "Tamanho: %s, Interface: %s e Capacidade: %s" %(self.tamanho,self.interface,self.capacidade) 

mp3 = MP3player(64) 
print(str(mp3)) 
input("End")