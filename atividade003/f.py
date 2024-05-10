# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 10/05/2024
# F) Faça um programa onde o usuário tenta adivinhar o número que o computador
# está ‘pensando’.

import random
import os


os.system('cls')

print('ADIVINHAÇÃO')
print('-' * 70)

numero = int(input('Insira um número de 1 a 10 e tente advinhar: '))
print()

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_sorteado = random.choice(lista_numeros)

if numero_sorteado == numero:
    print(f'Você acertou! O número sorteado foi: {numero} ='
          + f'{numero_sorteado}.')
else:
    print(f'Não foi dessa vez, o número correto era {numero_sorteado}.'
          + f'Tente novamente!')

print()
print('-' * 70)
