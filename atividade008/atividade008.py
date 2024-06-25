# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Dian Luca Valente Nascimento
# Turma: 0152
# Ano: 2024

# remove(elemento): Remove um elemento do set. Lança um erro se o elemento
# não estiver presente.
import os


os.system('cls')
frutas_set = set()

while True:
    print('UTILIZANDO O MÉTODO REMOVE()')
    print('-' * 70)
    # Adicionando valores a lista
    num_item = input('Quantos itens deseja inserir? ').strip()
    if num_item == '' or not num_item.isnumeric():
        num_item = 0
    else:
        num_item = int(num_item)
    
    for item in range(num_item):
        item = input(f'Insira a fruta {item + 1}: ').capitalize()
        if item == '' or not item.isalpha():
            print('Valor Inválido')
        else:
            frutas_set.add(item)
    
    os.system('cls')
    print('Item(ns) presentes no conjunto')
    print('-' * 70)
    if len(frutas_set) <= 0:
        print('Insira itens a lista')
    for item in frutas_set:
        print(item, end= ' | ')
    
    
    # Removendo
    print()
    print()
    remover = input('Qual item você deseja remover? ').capitalize().strip()
    if ((remover == ' ') or (remover not in frutas_set)):
        print('Valor inválido! Tente novamente.')
    else:
        frutas_set.remove(remover)
    
    os.system('cls')
    print('Item(ns) presentes no conjunto')
    print('-' * 70)
    for item in frutas_set:
        print(item, end= ' | ')
    
    print()
    print()
    continua = input('Deseja encerrar o programa? (s/n): ').lower().strip()
    if continua == 's':
        os.system('cls')
        break
    else:
        os.system('cls')