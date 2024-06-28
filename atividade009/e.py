# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# E - Faça um programa para criar um dicionário com 5  ferramentas. Depois, 
# imprima os valores e a quantidade de elementos do dicionário.
import os


os.system('cls')

ferramentas = {}

while True:
    print('FERRAMENTAS')
    num_item = input('Quantos itens deseja inserir: ')
    num_item = int(num_item)
    
    for c in range(num_item):
        print(f'Adicionando o item {c + 1}')
        chave = input('Insira uma chave: ')
        valor = input('Insira uma valor: ')
        os.system('cls')
        ferramentas[chave] = valor
        
    for chave, valor in ferramentas.items():
        print(f'{chave}: {valor}')
    
    num_ferramentas = len(ferramentas)
    print(f'Existem {num_ferramentas} itens no dicionário.')
    
    input('Enter para continuar. ')
    os.system('cls')