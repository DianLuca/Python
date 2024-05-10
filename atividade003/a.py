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
    print(f'O {numero} não possuí uma raiz real, pois retornará um valor complexo')
else:
    raiz = math.sqrt(numero)
    cima = math.ceil(raiz)
    baixo = math.floor(raiz)
    print(f'A raiz de {numero} é igual a: {raiz:.4f}, arredondando para cima: {cima:.2f} e para baixo: {baixo:.2f}')
    # if raiz == float:
        # cima = math.ceil(raiz)
        # baixo = math.floor(raiz)
        # print(f'A raiz de {numero} é igual a: {raiz}, arredondando para cima: {cima} e para baixo: {baixo}')
    # else:
        # print(f'A raiz de {numero} é igual a: {raiz:.2f}')
