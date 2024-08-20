# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que receba 2 listas:
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando
# como base essas duas listas. Depois, seu programa deverá imprimir esse
# dicionário utilizando uma estrutura de repetição for.
import os


os.system('cls')

# lista_1 = ['nome', 'peso', 'idade']
# lista_2 = ['John', '40', '1.8']
lista_unida = []


def unir(lista_1, lista_2):
    saida = dict(zip(lista_1, lista_2))
    lista_unida.append(saida)


def exibir():
    for item in lista_unida:
        for k, v in item.items():
            print(f'{k}: {v}', end=' | ')
    print()


while True:
    os.system('cls')
    print('|--- Criando um dicionário ---|')
    menu = input('1 - Criar um dicionário | 2 - Exibir Lista | 0 - Sair: ')
    if menu == '1':
        while True:
            os.system('cls')
            print('Criando uma lista')
            primeira_lista = input(
                'Insira os valores para as chaves separados por '
                'espaço: ').strip().split()
            segunda_lista = input(
                'Insira os respectivos valores de cada chave separados '
                'por espaço: ').strip().split()
            unir(primeira_lista, segunda_lista)
            break
    elif menu == '2':
        os.system('cls')
        print('Exibindo o dicionário')
        print()
        exibir()
        input('Pressione qualquer tecla para voltar ao menu. ')
    elif menu == '0':
        print('Programa Finalizado!')
        break
