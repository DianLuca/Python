# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# F - Faça um programa que cadastra 5 tipos de vinho. Para os campos deste 
# cadastro tome como referência nome do vinho, tipo, teor alcoólico e safra.
import os


os.system('cls')

tipo_vinhos = []
vinhos = {}

while True:
    print('CRIANDO UM DICIONÁRIO DE VINHOS')
    num_item = input('Quantos itens deseja inserir: ')
    num_item = int(num_item)
    
    print('Adicionando vinhos')
    for c in range(num_item):
        print(f'Adicionando o item {c + 1}:')
        vinhos['nome'] = input('Insira o nome do vinho: ')
        vinhos['tipo'] = input('Insira o tipo: ')
        vinhos['teor_alcoolico'] = input('Insira o teor alcoólico: ')
        vinhos['safra'] = input('Insira a safra: ')

        os.system('cls')
        tipo_vinhos.append(vinhos.copy())
        
    for vinho in tipo_vinhos:
        for chave, valor in vinho.items():
            print(f'{chave.capitalize()}: {valor}', end=' | ')
        print()
    
    input('Pressione Enter para continuar. ')