import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE CONTROLE COM INPUT E IF')
print('=' * 70)
print()

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º número: '))
    
    if (numero % 2 == 0):
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

print('-' * 70)
print()