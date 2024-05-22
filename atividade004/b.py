# Faça um programa que receba o nome 'João da Silva' e, em seguida, 
# substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

nome = 'João da Silva'

substituicao = nome.replace('da Silva', 'Oliveira')
print(f'O nome original é: {nome} e passará a ser: {substituicao}')