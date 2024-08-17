import os
from modulo_csv.funcoes_csv import ler_arquivo, escrever_arquivo, adicionar_arquivo

cadastro = []
registro = {}

# Lista para a exibição
lista = []


while True:
    os.system('cls')
    menu = input('1 - Cadastro | 2 - Alteração | 3 - Exclusão | 4 - Exibir | 0 - Sair: ')
    
    while menu == '1':
        nome = input('Insira o nome: ')
        idade = input('Insira a idade: ')
        registro['nome'] = nome
        registro['idade'] = idade
        cadastro.append(registro.copy())
        adicionar_arquivo(cadastro)
        input(f'O item "{nome}" foi adicionado com sucesso! ')
        break
    while menu == '2':
        pass
    while menu == '3':
        pass
    while menu == '4':
        os.system('cls')
        lista.clear() # Limpando a lista para não exibir nome duplicados
        for items in ler_arquivo(): # Lendo os dados do arquivo
            lista.append(items) # Criando uma lista para a leitura
        # Exibindo a lista completa
        print('-' * 70)
        print('nome\tidade')
        print('=' * 70)
        for item in lista:
            for v in item.values():
                print(f'{v}', end='\t')
            print()

        input('\nVoltar ao menu principal. ')
        break
    if menu == '0':
        print('Programa finalizado')
        break