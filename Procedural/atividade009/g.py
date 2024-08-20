# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024 

# G - Faça um programa para cadastrar os alunos de uma escola. Para os campos,
# tome como referência o nome do aluno, data de nascimento e matrícula.
import os


os.system('cls')
cadastro = []
alunos = {}

while True:
    print('CADASTRO DE ALUNOS')
    
    num_item = input('Quantos itens deseja adicionar: ')
    num_item = int(num_item)
    
    for c in range(num_item):
        print(f'Adicionando o {c + 1}º aluno:')
        alunos['nome'] = input('Insira o nome: ')
        alunos['data_nascimento'] = input('Insira a data de nascimento: ')
        alunos['matricula'] = input('Insira a matricula: ')
        os.system('cls')
        cadastro.append(alunos.copy())
        
    for aluno in cadastro:
        for chave, valor in aluno.items():
            print(f'{chave}: {valor}', end=' | ')
        print()
        