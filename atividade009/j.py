# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# J - Faça um programa para criar um dicionário com nomes de frutas. 
# Em seguida verifique se tem abacaxi nos valores.
import os


os.system('cls')

frutas = {}

while True:
    os.system('cls')
    print('Adicionando frutas:')
    num_item = input('Quantos itens deseja inserir? ')
    num_item = int(num_item)
    
    for c in range(num_item):
        print(f'Adicionando o {c + 1}º item:')
        chave = input('Insira a fruta: ')
        valor = input('Insira a quantidade: ')
        frutas[chave] = valor
        os.system('cls') 
    
    fruta = input('Qual fruta você deseja verificar na cesta: ')
    
    if fruta in frutas:
        print(f'A {fruta} está na cesta de frutas.')
    else:
        print(f'A {fruta} não está na cesta de frutas.')
    
    input('Pressione Enter para exibir toda a cesta de frutas: ')
    print('Itens no dicionário de frutas:')
    for chave, valor in frutas.items():
        print(f'{chave}: {valor}')
    print()
    
    input('Pressione Enter para continuar. ')
    