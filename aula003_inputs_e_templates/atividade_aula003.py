# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca
# Data: 17/04/2024
# Atividade de variáveis, template strings e casting

# Imports
import os


# Limpandoo terminal
os.system('cls')

print('-' * 70)
print('INSIRA OS DADOS SOLICITADOS')
print('=' * 70)

# Entrada
nome = input('Insira o seu nome: ')

# Entrada com Casting
idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura em metros: '))
atividade = bool(input('Você está fazendo algum curso no' 
+ 'momento?(Insira True ou False)'))
cidade = str(input('Em qual cidade você reside no momento? '))

# Saída Interpolada
print('-' * 70)
print(f'Oi {nome}, você tem {idade} anos e possui {altura} de altura. ' 
      + 'No momento seu status para realização de cursos é: {atividade}, '
      + 'e reside na cidade de {cidade}.')

print('-' * 70)

# Saída dos tipos das variáveis
print('A variável nome é do tipo.....:', type(nome))
print('A variável idade é do tipo....:', type(idade))
print('A variável altura é do tipo...:', type(altura))
print('A variável atividade é do tipo:', type(atividade))
print('A variável cidade é do tipo...:', type(cidade))

print('-' * 70)
print('')