import os

os.system('cls')

valor1 = input('Insira um valor:')
valor2 = input('Insira um valor:')
valor3 = input('Insira um valor:')

# Para maior
if valor1 > valor2 > valor3:
    print(f'O valor {valor1} é maior que os valores: {valor2} e {valor3}')
elif valor2 > valor1 > valor3:
    print(f'O valor {valor2} é maior que os valores: {valor1} e {valor3}')
else:
    print(f'O valor {valor3} é maior que os valores: {valor1} e {valor2}')


# Para menor
if valor1 < valor2 < valor3:
    print(f'O valor {valor1} é menor que os valores: {valor2} e {valor3}')
elif valor2 < valor1 < valor3:
    print(f'O valor {valor2} é menor que os valores: {valor1} e {valor3}')
else:
    print(f'O valor {valor3} é menor que os valores: {valor1} e {valor2}')
