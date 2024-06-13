# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na 
# posição correta.
import os


os.system('cls')

lista = [1, 2, 3, 5, 6]
print(f'Lista Original:{lista}')

inserir_lista = input(f'Qual valor devo inserir para completar a lista {lista}? ')

inserir_lista_completa = lista.insert(inserir_lista) # Retorna erro

print(f'Lista Ateradada: {lista}')

# Depois aplicar um input e utilizar sort()