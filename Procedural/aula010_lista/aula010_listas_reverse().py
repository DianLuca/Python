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

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')

# Solicita ao usuário para decidir se deseja inverter a lista
ordem = input('Deseja inverter a ordem da lista? [S/N]').strip().lower()

# Verifica a escolha do usuário e ordena a lista de acordo
if ordem == 's':
    numeros.reverse()
    print(f'Lista invertida: {numeros}')
else:
    print('Opção inválida! A lista não foi invertida.')
