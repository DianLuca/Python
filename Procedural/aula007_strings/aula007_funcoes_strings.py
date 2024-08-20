import os


os.system('cls')

print('-' * 70)
print('Funções String')
print('=' * 70)

frase = 'Olá, Mundo!'
quantidade_caracteres = len(frase) # conta os caracteres
print(f'A frase "{frase}" \n contém {quantidade_caracteres} caracteres')
print('.' * 70)

minusculas = frase.lower() # frase em minúsculo
print(f'Frase original: {frase}')
print(f'Frase nova: {minusculas}')
print('.' * 70)

maiusculas = frase.upper() # frase em maiúsculo
print(f'Frase original: {frase}')
print(f'Frase nova: {maiusculas}')
print('.' * 70)

captalizada = frase.capitalize() # frase capitalizada
print(f'Frase original: {frase}')
print(f'Frase nova: {captalizada}')
print('-' * 70)

frase1 = ' Olá, Mundo  '
sem_espacos = frase1.strip() # Retirar espaços, antes e depois
print(f'Frase original: {frase1}')
print(f'Frase nova: {sem_espacos}')
print('.' * 70)

substituicao = frase.replace('Mundo', 'Python') # Troca as palavras
print(f'Frase original: {frase}')
print(f'Frase nova: {substituicao}')
print('.' * 70)

lista = frase.split(',') # Separa as palavras de uma string em uma lista
print(f'Frase original: {frase}')
print(f'Frase nova: {lista}')
print('.' * 70)

lista = ['Olá', 'Mundo!']
juncao = ' '.join(lista) # Transforma uma lista em uma string com separador
print(f'Frase original: {lista}')
print(f'Frase nova: {juncao}')
print('.' * 70)