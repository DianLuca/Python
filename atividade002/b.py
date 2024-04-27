import os

os.system('cls')

valor1 = input('Insira um valor: ')
valor2 = input('Insira um valor: ')
valor3 = input('Insira um valor: ')
maior = float()
menor = float()

# Para maior
if valor1 > valor2 and valor1 > valor3:
    maior = valor1
elif valor2 > valor1 or valor2 > valor3:
    maior = valor2
elif valor3 > valor1 or valor3 > valor2:
    maior = valor3
else:
    print(f'Os valores são iguais')


# Para menor
if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor1 or valor2 < valor3:
    menor = valor2
elif valor3 < valor1 or valor3 < valor2:
    menor = valor3
else:
    print(f'Os valores são iguais')

print()
print(f'O maior valor será {maior} e o menor é {menor}')
print('-' * 70)