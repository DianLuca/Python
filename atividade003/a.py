# A) Faça um programa que receba um valor e mostre sua raiz quadrada. 
# Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos, avisando ao usuário que o 
# resultado será um número complexo.

import os
import math


os.system('cls')

print('RAIZ QUADRADA')
print()

numero = float(input('Insira um valor: '))

if numero < 0:
    print(f'O {numero} não possuí uma raiz real, pois retornará um valo' 
          + f'complexo')
else:
    raiz = math.sqrt(numero)
    arredondamento_para_cima = math.ceil(raiz)
    arredondamento_para_baixo = math.floor(raiz)
    print(f'A raiz de {numero} é igual a: {raiz:.4f}, arredondando para cima:' 
    + f'{arredondamento_para_cima:.2f} e para baixo:' 
    + f'{arredondamento_para_baixo:.2f}')
    # if raiz == float:
        # cima = math.ceil(raiz)
        # baixo = math.floor(raiz)
        # print(f'A raiz de {numero} é igual a: {raiz}, arredondando para cima: 
        # {cima} e para baixo: {baixo}')
    # else:
        # print(f'A raiz de {numero} é igual a: {raiz:.2f}')
