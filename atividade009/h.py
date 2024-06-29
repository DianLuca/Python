# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# H - Faça um programa para ler o dicionário nomes = {‘nome’: ’John, 
# ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}. Em seguida realize as seguintes
# ações:
# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura
import os


os.system('cls')

cadastro = []
pessoas = {}

while True:
    num_item = input('Quantos itens deseja inserir? ')
    num_item = int(num_item)
    
    for c in range(num_item):
        print('Adicionando pessoas:')
        pessoas['nome'] = input('Insira o nome: ')
        pessoas['idade'] = input('Insira a idade: ')
        pessoas['peso'] = input('Insira o peso: ')
        pessoas['altura'] = input('Insira a altura: ')
        os.system('cls')
        # cadastro.append(pessoas.copy())
    
    print('Itens inseridos para cadastrado:')
    for chave, valor in pessoas.items():
        print(f'{chave}: {valor}', end=' | ')
    print()
        
    input('Pressione Enter para continuar.')
       
    apagar = input('Qual dado deseja apagar algum dos dados? ')
    removido = pessoas.pop(apagar, 'Elemento não encontrado.')
    print(f'O elemento {removido}')
    cadastro.append(pessoas.copy())
    
    os.system('cls')
    
    print('Itens cadastrados após remoção:')
    for pessoa in cadastro:
        for chave, valor in pessoa.items():
            print(f'{chave}: {valor}', end=(' | '))
        print()
    
    input('Pressione Enter para continuar.')
    os.system('cls')