# Faça um programa que receba uma frase e, em seguida, 
# mostre quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

frase = input('Insira uma frase: ').lower()

letra_a = frase.count('a')
letra_e = frase.count('e')
letra_i = frase.count('i')
letra_o = frase.count('o')
letra_u = frase.count('u')

soma_caracteres = letra_a + letra_e + letra_i + letra_o + letra_u

print(f'As vogais aparecem: \n VOGAL A(a): {letra_a} \n VOGAL E(e): {letra_e}'
      + f'\n VOGAL I(i): {letra_i} \n VOGAL O(o): {letra_o} \n '
      + f'VOGAL U(u): {letra_u} \n e somam {soma_caracteres} caracteres')