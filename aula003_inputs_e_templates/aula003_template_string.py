# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Dian Luca Valente Nascimento
# Data: 16/04/2024

# imports
# Biblioteca para interagir o SO
import os
#Biblioteca para pegar date e hora do sistema
import datetime


# Limpando o terminal
os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS EM PYTHON')
print('=' * 70)

# Entrada
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('Entre com a altura: ')

# Entrada com Casting
nascimento = int(input('Data de Nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre com o Bairro: '))
rua = str(input('Nome da Rua: '))
numero = int(input('Entre com o numero: '))

# Processamento: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento 

# Saída
print('-' * 70)
print('SAÍDA DE DADOS')
print('=' * 70)
print('Nome..............: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............: ', peso)
print('Altura............: ', altura)

#Saída Interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP.......: {cep}')
print(f'Bairro....: {bairro}')
print(f'Rua.......: {rua}')
print(f'Número....: {numero}')
print('-' * 70)
print('')