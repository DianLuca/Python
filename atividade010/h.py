# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a
# média de altura  e peso de seus clientes. Faça um programa que pergunte a
# cada um dos clientes da academia seu código, nome, altura e peso. Após esse
# cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de
# clientes é indefinido. Veja a saída no próximo slide.
import os


os.system('cls')

clientes = []
cliente = {}


def cadastro(codigo, nome, altura, peso):
    cliente['codigo'] = codigo
    cliente['nome'] = nome
    cliente['altura'] = altura
    cliente['peso'] = peso
    clientes.append(cliente.copy())


def media_peso_altura():
    soma_altura = 0
    soma_peso = 0
    for aluno in clientes:
        soma_altura += aluno['altura']
        soma_peso += aluno['peso']
    media_altura = soma_altura / len(clientes)
    media_peso = soma_peso / len(clientes)
    return media_altura, media_peso


while True:
    print('|--- ACADEMIA ---|')
    for aluno in clientes:
        for k, v in aluno.items():
            print(f'{k}: {v}', end=' | ')
        print()
    menu = input('1 - Cadastrar | 2 - Média de Peso e Altura | 0 - Sair : ')
    os.system('cls')
    if menu == '1':
        while True:
            print('MENU DE CADASTRO')
            codigo = input('Insira o seu código: ')
            nome = input('Insira o seu nome: ')
            altura = float(input('Insira o sua altura: '))
            peso = float(input('Insira o seu peso: '))
            cadastro(codigo, nome, altura, peso)
            os.system('cls')
            break
    elif menu == '2':
        peso_media, altura_media = media_peso_altura()
        print('A média de peso e altura geral da academia: ')
        print(f'Peso: {peso_media}')
        print(f'Altura: {altura_media}')
        input('Para voltar ao menu pressione ENTER: ')
        os.system('cls')
    elif menu == '0':
        break
    else:
        print('Opção inválida!')
