# Faça um programa para sortear um número de 1 a 20.

import random
import os


os.system('cls')

print('SORTEIO')
print('-' * 70)

minimo = int(input('Insira um valor inteiro mínimo: '))
maximo = int(input('Insira um valor inteiro máximo: '))

# Adicionar validação para valor que inconsistente max < min, por exemplo

sorteando = random.randint(minimo, maximo)

print(f'O valor sorteado foi: {sorteando}')