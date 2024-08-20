# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os


os.system('cls')

notas = []
soma = 0

entrada = input('Insira as notas sepadaras por vírgula: ').replace(' ', '') # Permite a inserção de vários valores, e remove o espaço entre eles

notas_trimestre = entrada.split(',') # Define por qual caracter eles serão separados
notas.extend(notas_trimestre) # Envia para adicionar a lista de notas

for nota in notas:
    soma += float(nota) # Soma todas as notas
    
periodos = len(notas) # Conta o números de itens na lista
media = (soma / periodos) 

print()
print(f'A média das notas nos {periodos} período(s) foi de: {media:.2f}.')