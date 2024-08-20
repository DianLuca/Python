# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

# Crie uma função que verifica se uma aluno está cadastrado ou não em um
# dicionário. Se estiver cadastrado, imprima o nome desse aluno e o resto dos
# seus dados. O dicionário deverá conter nome, matrícula e a data de
# nascimento do aluno.
import os


os.system('cls')

cadastro = []
aluno = {}


def encontrar(aluno):
    for alunos in cadastro:
        if aluno in alunos['nome']:
            print(f'O aluno: {aluno} está na lista!')
            for k, v in alunos.items():
                print(f'{k}: {v}', end=' | ')
        else:
            print(f'O aluno: {aluno} não está presente.')


def exibir():
    if cadastro:
        for item in cadastro:
            for k, v in item.items():
                print(f'{k}: {v}', end=' | ')
            print()
    else:
        print('O cadastro está vazio!')


def cadastrar(**aluno):
    alunos = aluno
    cadastro.append(alunos.copy())


while True:
    os.system('cls')
    print('CADASTRO DE ALUNOS')
    menu = input('1 - CADASTRAR | 2 - EXIBIR | 3 - BUSCAR | 0 - SAIR: ')
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
        print()
        input('Pressione Enter')
    elif menu == '3':
        aluno = input('Insira o nome para ser verificado: ')
        encontrar(aluno)
        print()
        input('Pressione Enter')
    elif menu == '0':
        print('Encerrando o sistema!')
        break
