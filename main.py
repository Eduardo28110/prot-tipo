from classe import *
from views import *

lista_de_cao = []
lista_de_pessoa = []

def criar_cao():
    nome = input("nome do cão: ")
    tamanho = input("tamanho em cm: ")
    raca = input("raça do cão: ")
    cao = Cachorro(nome,tamanho,raca)
    lista_de_cao.append(cao)

def criar_pessoa():
    nome = input("nome do humano: ")
    tamanho = input("peso do humano: ")
    peso = input("peso do humano: ")
    lista_de_pessoa.append(pessoa)


while True:
    print(menu_principal())  
    op = int(input("Informe uma opção: "))
    if 1 == op:
        criar_cao

    elif 2 == op:  
        criar_pessoa()
