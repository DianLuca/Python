# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo
# em tela esse resultado.
import os


os.system('cls')

print('-- VERFICAÇÃO DE PALÍNDROMO --') # Quando um nome ou uma frase é 
                                        # igual mesmo ao contrário
nome = input('Insira seu nome ou uma frase: ')
palindromo = nome[::-1]

if nome == palindromo:
    print(f'Trata-se de um palíndromo, pois {nome} e {palindromo} ' 
          + f'são iguais.')
else:
    print(f'Não se trata de um palíndromo pois {nome} e {palindromo} '
          + f'formam palavras diferentes')