# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os


os.system('cls')

nomes = []

for i in range(0, 5): # Será inserido 5 nomes
    nome = input('Insira um nome: ')
    nomes.append(nome)

print()
print('Lista de Nomes: ')
for indice, nome in enumerate(nomes, start = 1): # Irá enumerar cada índice começando em 1
    pessoas = f'{indice}: {nome}'
    print(pessoas)