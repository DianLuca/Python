import os


os.system('cls')

print('-' * 70)
print('ESTRUTURA DE DADOS: DICIONÁRIOS') # dict => {}
print('=' * 70)

# Índices iguais: só irá exibir um item
dicionario_1 = {'nome': 'John', 'nome' : 'Jane'}

# Posso ter uma tupla como índice e uma lista como valor
dicionario_2 = {(1, 2) : [1, 2]}

# Mas não posso ter uma lista como índice e uma tupla como valor
# dicionario_3 = {[1, 2] : (1, 2)} # ERROR

# Saída
print('-' * 80)
print(dicionario_1)
print(dicionario_2)

print()