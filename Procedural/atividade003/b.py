# Faça um programa que receba 2 valores, faça a divisão entre eles. Se a 
# divisão não for inteira, o programa deverá arredondar o resultado para cima
# e para baixo. Faça a validação para divisão por 0.

import os
import math


os.system('cls')


print('DIVISÃO')
print()
dividendo = float(input('Insira um valor: '))
divisor = float(input('Insira um valor: '))
resposta = ''

if divisor == 0:
    resposta = f'Valor Inválido! Não é possível fazer divisão por {divisor}.'
else:
    resto = dividendo / divisor
    arredondando_para_cima = math.ceil(resto)
    arredondando_para_baixo = math.floor(resto)
    resposta = (f'O resto da divisão entre {dividendo} e {divisor} é: {resto}. ' 
                + f'Arredondado para cima: {arredondando_para_cima} e '
                + f'para baixo: {arredondando_para_baixo}')

print()
print(resposta)
print('-' * 70)