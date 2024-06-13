# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na 
# posição correta.
import os


os.system('cls')

lista = [1, 2, 3, 5, 6] 
print(f'Lista Original:{lista}') # A lista original não possui o número '4'

inserir_lista = input(f'Qual valor devo inserir para completar a lista {lista}? ') # Entrada do usuário

inserir_lista_completa = lista.append(int(inserir_lista)) # Inserindo valor na lista
lista.sort() # Colocando o valor na ordem correta

print()
print(f'Lista Ateradada: {lista}')

# Depois aplicar um input e utilizar sort()