import os 


os.system('cls')

print('-' * 70)
print('SAÍDA COM FOR... ENUMERATE()')
print('=' * 70)

soma = 0

# Criando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o enumerate() O comando enumerate adiciona
# um índice para cada valor dde nossa lista start opcional, para não
# começar no índice 0 ex.: enumerate(lista_numeros, start = 1)

# Para cada número dentro da lista de números, enumere com um índice
for indice, numero in enumerate(lista_numeros):
    soma += numero
    print(f'Índice: {indice} = Número: {numero}')

print('-' * 70)
print(f'A soma de todos os números é: {soma}')
print('-' * 70)