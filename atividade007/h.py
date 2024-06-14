# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que sorteia os números da Mega-Sena e da Lotofácil
import os
import random


os.system('cls')

numeros_mega = [] # Mega-Sena [1 a 60]
numeros_lotofacil = [] # Lotofácil [1 a 25]

for i in range(1, (60 + 1)):
    i = int(i)
    numeros_mega.append(i)
    if i <= 25:
        numeros_lotofacil.append(i)

# SORTEANDO
sorteio_mega = random.sample(numeros_mega, 6) # Retorna os 6 valores necessários, .sample
sorteio_lotofacil = random.sample(numeros_lotofacil, 15) # Retorna os 15 valores necessários

sorteio_mega.sort() # Apenas ordenando pra ficar bonitinho
sorteio_lotofacil.sort()

print(f'Os números sorteados na MEGA-SENA: {sorteio_mega}')
print()
print(f'Os números sorteados na LOTOFÁCIL: {sorteio_lotofacil}')
