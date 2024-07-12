# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando 
# como base essas duas listas. Depois, seu programa deverá imprimir esse 
# dicionário utilizando uma estrutura de repetição for.
import os


os.system('cls')

lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['John', '40', '1.8']
lista_unida = []

def unir():
    saida = dict(zip(lista_1, lista_2))
    lista_unida.append(saida)
    for k, v in saida.items():
        print(f'{k}: {v}', end=' | ')
    print()

unir()
input('continue')