# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que some a quantidade de números pares encontrados 
# no intervalo entre 0 e 100.
import os 


os.system('cls')

print('SOMATÓRIO DE NÚMEROS PARES')
print()

a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
print()

c_par = 0
soma = 0

for c in range(a, (b + 1)):
    par = c % 2 == 0
    if par == True:
        print(c, end=' | ')
        c_par += 1
        soma += c
print()
print(c_par)
print(soma)