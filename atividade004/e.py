# Faça um programa que receba uma frase e, em seguida, 
# mostre quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

frase = input('Insira uma frase: ')

vogal = 'aeiouAEIOU'

conta = frase.count(vogal)
print(conta)

# if 'aeiouAEIOU' in frase:
    # print(f'A frase "{frase}" possui caracteres que são vogais.')
# else:
    # print('Corrigir o código!')