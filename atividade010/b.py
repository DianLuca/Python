# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de
# nascimento. Depois imprima os resultados cadastrados utilizando uma
# estrutura de repetição for.
import os


os.system('cls')

cadastro = []
alunos = {}


def cadastrar(**aluno):
    alunos = aluno
    cadastro.append(alunos.copy())


def exibir():
    for item in cadastro:
        for k, v in item.items():
            print(f'{k}: {v}', end=' | ')
        print()


while True:
    os.system('cls')
    print('CADASTRO DE ALUNOS')
    menu = input('1 - CADASTRAR | 2 - EXIBIR | 0 - SAIR: ')
    if menu == '1':
        while True:
            nome = input('Insira o nome do aluno: ').title().strip()
            matricula = input('Insira o nome do matricula: ')
            data_de_nascimento = input('Insira o nome do data de nascimento: ')
            cadastrar(nome=nome, matricula=matricula,
                data_de_nascimento=data_de_nascimento)
            break
    elif menu == '2':
        exibir()
        input('Pressione Enter')
    elif menu == '0':
        print('Encerrando o sistema!')
        break
