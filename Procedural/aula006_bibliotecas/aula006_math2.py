import math
import os


os.system('cls')

print('-' * 50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('=' * 50)
print()

numero_decimal = float(input('Entre com um número decimal: '))

arrendonda_para_cima = math.ceil(numero_decimal)
arrendonda_para_baixo = math.floor(numero_decimal)

print('-' * 50)
print(f'O número {numero_decimal} arredondado para cima é.: '
      + f'{arrendonda_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é: '
      + f'{arrendonda_para_baixo}')
print('-' * 50)
