class Animal:
    nome = str
    tamanho = True
    coracao: bool

    def __init__(self,nome, tamanho, coracao):
        self.nome = nome
        self.tamanho = tamanho
        self.coracao = coracao

    def info(self):
        return {'nome':self.nome}
 
class Humano(Animal):
    def __init__(self,nome, tamanho, peso):
        super().__init__(nome,True, True)
        self.nome = nome
        self.tamanho = tamanho
        self.peso = peso

class Cachorro(Animal):
    tamanho = 0
    raca = ''

    def __init__(self,nome,tamanho,raca):
        super().__init__(nome,True,False)
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca