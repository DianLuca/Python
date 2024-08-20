import os


os.system('cls')

valor = int(input('Insira um valor inteiro:'))
resposta = ''

if valor % 2 == 0:
    print()
    print(f'O {valor} é um número par.')
else:
    print()
    print(f'O {valor} é um número ímpar.')

print('-' * 70)
print('FIM DO PROGRAMA')
print()