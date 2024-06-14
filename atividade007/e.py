# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024 
# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os


os.system('cls')

lista_nomes = []

entrada = input('Insira 6 nomes separados por vírgula: ').strip()

nome = entrada.split(',')
lista_nomes.extend(nome)

if ('Pedro' in lista_nomes):
    print(f'Lista nomes: {lista_nomes}')
    print()
    print('O nome "Pedro" está na lista.')
else:
    print()
    print('O nome "Pedro" não está na lista.')