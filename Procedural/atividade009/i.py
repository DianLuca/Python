# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# I - Faça um programa para criar um dicionário com 4 elementos. Depois 
# imprima a lista completa, delete o último elemento e mostre uma 
# listagem nova.
import os


os.system('cls')

lista_elementos = []
elementos = {}

while True:
    print('Adicionando elementos.')
    num_item = input('Quantos items deseja adicionar? ')
    num_item = int(num_item)
    
    for c in range(num_item):
        print(f'Adicionando o {c + 1}º elemento:')
        elementos['nome'] = input('Insira um nome: ')
        elementos['idade'] = input('Insira a idade: ')
        os.system('cls')
        lista_elementos.append(elementos.copy())
    
    for elemento in lista_elementos:
        for chave, valor in elemento.items():
            print(f'{chave}: {valor}', end=' | ')
        print()
        
    print()
    print('O último item inserido será removido.')
    input('Pressione Enter para continuar. ')
    os.system('cls')
    
    lista_elementos.pop()
            
    for elemento in lista_elementos:
        for chave, valor in elemento.items():
            print(f'{chave}: {valor}', end=' | ')
        print()
    
    print()
    input('Pressione Enter para continuar. ')
    os.system('cls')