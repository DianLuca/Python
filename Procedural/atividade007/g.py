# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que gere 10 números aleatórios. 
# Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os
import random


os.system('cls')

inicio = int(input('Insira um valor inteiro: '))
final = int(input('Insira outro valor inteiro: '))

# "_" é utilizado, pois não importa os valores 
# gerados no intervalo, só é necessários que eles sejam inseridos. 
# Ou seja, ele começa como um valor vazio (?)
lista_numeros = [random.randint(inicio,final) for _ in range(10)]

lista_asc = []
lista_desc = []

lista_asc.extend(lista_numeros)
lista_desc.extend(lista_numeros)

lista_asc.sort()
lista_desc.sort(reverse = True)

print()
print(f'Lista ordenada ascendente: {lista_asc}')
print(f'Lista ordenada descendente: {lista_desc}')
