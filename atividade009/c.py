# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# C - Utilizando o exercício anterior, retire um elemento do dicionário.
import os


os.system('cls')

elementos = {}

while True:
    num_item = input('Quantos itens deseja adicionar: ')
    num_item = int(num_item)
    os.system('cls')
    
    # Adicionando valores
    for c in range(num_item):
        print(f'Adicionando o item {c + 1}')
        chave = input('Insira uma chave: ')
        valor = input('Insira uma valor: ')
        os.system('cls')
        elementos[chave] = valor
    
    print('Itens do dicionário:')
    for chave, valor in elementos.items():
        print(f'{chave.capitalize()}: {valor}', end=' | ')
        
    print()
    input('\nPressione Enter para continuar. ')
    
    apagar = input('Qual item deseja apagar? ')
    removido = elementos.pop(apagar, f'{apagar} não está presente na lista.')
    print(f'Item removido {apagar}: {removido}')
        
    input('Pressione Enter para continuar. ')
        