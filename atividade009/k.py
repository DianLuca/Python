# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024

# K - Faça um programa que peça continuamente o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999, o programa será finalizado e executará
# uma impressão com os nomes cadastrados.
import os


os.system('cls')

pessoas = {}

while True:
    print('Adicionando pessoas:')
    print()
    chave = input('Insira um nome: ')
    valor = input('Insira a idade (999 - Encerra o programa): ')
    pessoas[chave] = valor

    if valor == '999':
        os.system('cls')
        print('Todos as pessoas na lista:')
        for chave, valor in pessoas.items():
            print(f'{chave.capitalize()}: {valor}')
        print()
        input('Pressione Enter para encerrar o programa. ')
        break
    else:
        os.system('cls')
