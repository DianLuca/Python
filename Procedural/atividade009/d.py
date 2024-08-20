# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# D - Faça um programa para criar um dicionário com 5  cores. Depois,  imprima
# as chaves e os valores deste dicionário.
import os


os.system('cls')

cores = {}
while True:
    print('ADICIONANDO CORES')
    num_item = input('Quantos itens deseja adicionar: ')
    num_item = int(num_item)

    for c in range(num_item):
        print(f'Adicionando a {c + 1}ª cor:')
        chave = input('Digite uma chave: ')
        valor = input('Digite uma valor: ')
        os.system('cls')
        cores[chave] = valor

    print()
    print('Dicionário de cores:')
    for chave, valor in cores.items():
        print(f'{chave}: {valor}')
    
    print()
    input('Pressione Enter para continuar. ')
    os.system('cls')