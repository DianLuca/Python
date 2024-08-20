# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.
import os


os.system('cls')

numeros_inteiros = [] # Lista vazia
soma = 0

for i in range(0, 5): # Vezes em que será solicitado para inserir o valor
    numeros = int(input('Insira um número inteiro: ').strip()) # Inserindo valores
    numeros_inteiros.append(numeros) 
    soma += numeros

print()
print(f'Compõem a lista os valores: {numeros_inteiros} e a soma entre eles é de: {soma}')