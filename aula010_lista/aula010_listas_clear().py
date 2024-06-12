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

# Solicita ao usuário para decidir se deseja limpar a lista
escolha = input('Deseja limpar a lista? [S/N]').strip().lower()

# Verifica a escolha do usuário e limpa a lista
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')
