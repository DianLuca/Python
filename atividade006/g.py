# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista
import os


os.system('cls')

lista_numeros = []

entrada = input('Insira 10 valores separados por vírgula: ').replace(' ','')

numeros = entrada.split(',')

lista_numeros.extend([int(numero) for numero in numeros])
# Converte o número para inteiro e fazer a ordenação de forma correta

lista_numeros.sort()

print()
print(f'Lista completa: {lista_numeros}')
menor = lista_numeros[0]
maior = lista_numeros[-1]
print()
print(f'O menor número da lista é: {menor} e o maior: {maior}')