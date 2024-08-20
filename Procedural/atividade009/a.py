# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 01/07/2024

# A - Faça um programa para criar um dicionário com 4 elementos.
import os


os.system('cls')

elementos = {}

print('ADICIONADO ELEMENTOS')

num_item = input('Quantos itens deseja inserir? ')

num_item = int(num_item)

# Adicionando o número de itens desejado
for c in range(num_item):
    print(f'Adicionando item {c + 1}')
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    elementos[chave] = valor

# Exibindo valores adicionados
print(elementos)
  

for chave, valor in elementos.items():
    print(f'{chave.capitalize()}: {valor}', end=' | ')