# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Evolua o programa anterior para um código que pergunte ao usuário qual o 
# intervalo que ele deseja ver  impresso.
import os


os.system('cls')

print('QUAL O INTERVALO DESEJADO')
a = int(input('Insira o valor inicial: '))
b = int(input('Insira o valor fim....: '))

c = 0

for c in range(a, (b + 1)):
    print(c, end =' - ')
    c += 1