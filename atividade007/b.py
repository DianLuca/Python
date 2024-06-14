# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Após esta entrada de dados, faça o seguinte: • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas. • Exiba todas as notas na ordem inversa à 
# que foram informadas, uma abaixo da outra. • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
import os


os.system('cls')

notas = []
soma = 0

entrada = input('Insira as notas separadas por espaço: ').strip()

nota = entrada.split()
notas.extend(nota)

quantidade_notas = len(notas)
print(f'Foram inseridas {quantidade_notas} notas') # Quantidade de notas inseridas
print()
print(f'As notas são: {notas}') # Notas inseridas
print()

inverso_notas = notas[::-1] # Invertendo a ordem da lista
# print(inverso_notas) # Também exibe a lista ao contrário mas não quebra a linha
print('Na ordem inversa e sobrepostas elas ficam dessa forma: ')
for nota in inverso_notas: # Imprimindo na ordem inversa a da inserção
    print(nota)


for nota in notas: # Somando as notas
    soma += int(nota) 

print()
print(f'Soma total das notas: {soma}')
media = soma / quantidade_notas # média das notas
print()
print(f'Média das notas: {media:.2f}')