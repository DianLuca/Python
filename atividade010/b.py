# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 12/07/2024

#Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de 
# nascimento. Depois imprima os resultados cadastrados utilizando uma 
# estrutura de repetição for.
import os


os.system('cls')

cadastro = []
alunos = {}

def cadastrar():
    alunos['nome'] = input('Insira o nome do aluno: ')
    alunos['matricula'] = input('Insira o nome do matricula: ')
    alunos['data_de_nascimento'] = input('Insira o nome do data de nascimento: ')
    
    os.system('cls')
    cadastro.append(alunos.copy())

while True:
    cadastrar()
    for aluno in cadastro:
        for k, v in aluno.items():
            print(f'{k}: {v}', end=' | ')
        print()

    input('Pressione Enter')