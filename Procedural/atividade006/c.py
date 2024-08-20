# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9 || • O intervalo de 8 até 13 || • Os números pares || • Os números ímpares
# • Os múltiplos de 2, 3 e 4 || • Lista reversa || • O produto dos intervalos 5-6 por 11-12
import os


os.system('cls')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print('O intervalo de 1 a 9: ')
for i in range(len(lista_numeros) + 1):
    if i <= 9:
        print(i, end = ', ')

print()
print('\nO intervalo de 8 a 13: ')
for i in range(len(lista_numeros) + 1):
    if 8 <= i <= 13:
        print(i, end =', ')

print()
print('\nOs números pares: ')
for i in range(len(lista_numeros) + 1):
    if i % 2 == 0:
        print(i, end=', ')

print()
print('\nOs números ímpares:')
for i in range(len(lista_numeros) + 1):    
    if i % 2 != 0:
        print(i, end=', ')

print()
print('\nOs múltiplos de 2, 3 e 4: ')
divisao_2 = [i for i in lista_numeros if i % 2 == 0] # i dentro do intervalo de i na lista_numeros, na condição if i % 2 == 0.
print(f'Esses números são divisíveis por 2: {divisao_2}') # O mesmo se repete nas outras condições.

divisao_3 = [i for i in lista_numeros if i % 3 == 0]
print(f'Esses números são divisíveis por 3: {divisao_3}')

divisao_4 = [i for i in lista_numeros if i % 4 == 0] 
print(f'Esses números são divisíveis por 4: {divisao_4}')

print()
print('Lista reversa: ')
lista_numeros.sort(reverse = True)
print(f'A lista reversa: {lista_numeros}')

print()
print('O produto dos intervalos 5-6 por 11-12: ')
produto_5_6 = [i for i  in lista_numeros if 5 <= i <= 6] # Nesse caso pega apenas 5 e 6 encontrados no intervalo
print(f'São produtos do intervalo de 5 e 6: {produto_5_6}')
produto_11_12 = [i for i  in lista_numeros if 11 <= i <= 12] # Nesse caso pega apenas 11 e 12 encontrados no intervalo
print(f'São produtos do intervalo de 11 e 12: {produto_11_12}') 

produto_total = produto_5_6[0] * produto_11_12[0] # Multiplica os valores encontrados nos respectivos índices
produto_total_1 = produto_5_6[1] * produto_11_12[1]
print(f'São produtos desses dois intervalos: {produto_total, produto_total_1}')
print()
# # EM DÚVIDA SOBRE QUAL MÉTODO É O CORRETO (CASO ACIMA), FAZENDO OUTRO MODELO (SERÁ ADOTADO O MODELO ACIMA):
# print('O produto dos intervalos 5-6 por 11-12: ')
# produto_5_6 = [i * i for i  in lista_numeros if 5 <= i <= 6] # Nesse caso multilica os valores encontrados no intervalo
# print(f'São produtos do intervalo de 5 e 6: {produto_5_6}')
# produto_11_12 = [i * i for i  in lista_numeros if 11 <= i <= 12] # Nesse caso multilica os valores encontrados no intervalo
# print(f'São produtos do intervalo de 11 e 12: {produto_11_12}') 

# produto_total = produto_5_6[0] * produto_11_12[0] # Multiplica os valores encontrados nos respectivos índices
# produto_total_1 = produto_5_6[1] * produto_11_12[1]
# print(f'São produtos desses dois intervalos: {produto_total, produto_total_1}')
# print()