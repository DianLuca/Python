# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os
import random # Para gerar números aleatórios


os.system('cls')

inicio = int(input('Insira um valor inteiro para sortear: '))
final = int(input('Insira outro valor inteiro para sortear: '))

# Gera 50 números aleatórios na lista. "_" (Valor vazio) é utilizado, pois não importa os valores 
# gerados no intervalo, só é necessários que eles sejam inseridos.
lista_numeros = [random.randint(inicio,final) for _ in range(50)] 


lista_fatiada = []

for i in range(1, 51, 10): 
    if i + 10 <= len(lista_numeros): # Enquanto não for menor ou igual a 10 não criará uma sublista
        lista = lista_numeros[i:i+10] # Verifica o número de itens na lista e quebra caso aconteça
        lista_fatiada.append(lista) # Insere na lista
    else:
        lista = lista_numeros[i:]
        lista_fatiada.append(lista)

for indice, lista in enumerate(lista_fatiada, start= 1): # Cria uma lista enumerada com 10 itens
    print(f'{indice}: {lista}')