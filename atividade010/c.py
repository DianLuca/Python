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

cadastro = [
    {'nome': 'Dian', 'matricula': '007', 'data_nascimento': '00/00/0000'}
]
aluno = {}

def encontrar():
    aluno = input('Insira o nome para ser verificado: ')
    for alunos in cadastro:
        if aluno in alunos['nome']:
            for k, v in alunos.items():
                print(f'{k}: {v}', end=' | ')
        else:
            print(f'O {aluno} não está presente')

while True:
    encontrar()
    print()
    input('Enter para continuar ')