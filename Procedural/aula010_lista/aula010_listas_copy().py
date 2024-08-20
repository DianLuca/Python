import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para decidir se deseja criar uma cópia da lista
escolha = input('Deseja inverter a ordem da lista? [S/N]').strip().lower()

# Verifica a escolha do usuário e ordena a lista de acordo
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Cópia da lista: {lista_copiada}')
else:
    print('A lista não foi copiada.')

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')
