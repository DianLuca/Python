# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 26/04/2024
# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação
# de anos bissextos para auxiliar usuários na identificação desses anos de
# forma rápida e precisa. Eles precisam de um programa que permita aos
# usuários inserir um ano e, em seguida, determine se esse ano é bissexto ou
# não, de acordo com as regras estabelecidas pelo calendário gregoriano.
# Além disso, é necessário realizar a validação de entrada de dados para
# garantir que o ano inserido pelo usuário seja um valor válido, ou seja, um
# número inteiro positivo.

# Import
import os


os.system('cls')

# Entrada
ano = int(input('Insira um ano: '))
resposta = ''

# Condicionais
if ano < 0:
    resposta = f'O {ano} inserido é um valor inválido'
elif ano % 4 == 0:
    resposta = f'O ano {ano} é um ano bissexto'
else:
    resposta = f'O ano {ano} não é um ano bissexto'

# Saída
print()
print(resposta)
print('-' * 70)