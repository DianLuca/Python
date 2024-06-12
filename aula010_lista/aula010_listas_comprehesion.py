import os 


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: LIST COMPREHESIONS [] - TRIPLICANDO VALORES')
print('=' * 70)

lista_numeros = [1, 2, 3, 4, 5]

# Triplicar os valores
lista_nova_triplicada = []

for item in lista_numeros:
    lista_nova_triplicada.append(item * 3)

print('Triplicar os valores: forma normal')
print(f'Lista triplicada: {lista_nova_triplicada}')
print()

# List Comprehesions
lista_nova_triplicada_2 = [item * 3 for item in lista_numeros]
print('Triplicar os valores: List Comprehensions')
print(f'Lista triplicada: {lista_nova_triplicada_2}\n')