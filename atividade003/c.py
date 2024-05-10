# Faça um programa que receba as informações de base e expoente. 
# Calcule a potência.

import os
import math


os.system('cls')

print('POTENCIAÇÃO')
print('-' * 70)

base =  float(input('Insira um valor para a base....: '))
expoente = float(input('Insira um valor para o expoente: '))

potencia = math.pow(base, expoente)

print(f'O resultado da potenciação entre {base} e {expoente} é: {potencia}')