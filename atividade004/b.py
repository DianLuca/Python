# Faça um programa que receba o nome 'João da Silva' e, em seguida, 
# substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

nome = input('Insira um nome: ').lower()

print(nome)
print()
print(nome.replace(' ',''))
print()
# Validação
if not (nome.replace(' ','').isalpha()):
    print('O item possui um caracter inválido!')
elif 'silva' in nome:
    substituicao = nome.replace('silva', 'Oliveira')
    print(f'O nome original é: {nome.title().strip()} e passará a ser: {substituicao.title().strip()}')
else:
    print(f'Não foi encontrado o nome "Silva" para realizar a substituição.')
    
