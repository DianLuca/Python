# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024

# B - Utilizando o exercício anterior,  adicione mais 2 elementos ao 
# dicionário.
import os


os.system('cls')

elementos = {}

while True:
    num_item = input('Quantos itens deseja adicionar: ')
    num_item = int(num_item)

    for c in range(num_item):
        print(f'Adicionando item {c + 1}')
        chave = input('Insira uma chave: ')
        valor = input('Insira um valor: ')
        os.system('cls')
        elementos[chave] = valor
        
    print(elementos)

    print('Elementos no dicionário:')
    for chave, valor in elementos.items():
        print(f'{chave}: {valor}', end=' | ')
        
    input('\nEnter para continuar')
    os.system('cls')