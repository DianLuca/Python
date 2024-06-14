# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024 
# Faça um programa que recebe 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares. 
import os


os.system('cls')

lista_numeros = []

entrada = input('Insira sete números aleatórios separados por espaço: ').strip()

numeros = entrada.split()
lista_numeros.extend(numeros)

pares = []
impares = []

for i in lista_numeros:
    i = int(i)
    if i % 2 == 0:
        pares.append(int(i))
    else:
        impares.append(int(i))
        
print(f'Os números pares que compõem a lista são: {pares}')
print(f'Os números ímpares que compõem a lista são: {impares}')
