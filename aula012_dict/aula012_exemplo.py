import os


os.system('cls')

# iniciando do dicionário e da lista
elementos = {} # Dicionário
periodica = [] # Lista

# Entrada de dados
for c in range(2):
    print(f'Entrada de dados {c + 1}:')
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adiciona os dados ao dicionário
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    # Usa append() com copy() para adicionar uma cópia do dicionário à lista
    periodica.append(elementos.copy())
    
print()
print('-' * 70)
print('Elementos na tabela periódica: ')
print(periodica)
print('-' * 70)
print()

# For anhinhado para percorrer a lista e o dicionário
print('Detalhes dos elementos:')
for dicionario in periodica: # Para cada elemento na lista
    for chave, valor in dicionario.items(): # Para chave e valor do dicionário
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legível
    print('-' * 70)
    