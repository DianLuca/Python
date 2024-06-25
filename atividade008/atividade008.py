# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Dian Luca Valente Nascimento
# Turma: 0152
# Ano: 2024

# remove(elemento): Remove um elemento do set. Lança um erro se o elemento
# não estiver presente.
import os


os.system('cls')
valores_set = set() # Iniciando um conjunto vazio

while True:
    print('UTILIZANDO O MÉTODO REMOVE()')
    print('-' * 70)
    # Adicionando valores a lista para ter itens para excluir
    num_item = input('Quantos item(ns) deseja inserir? ').strip()
    # Validando entrada
    if ((num_item == '') or not (num_item.isnumeric())):
        num_item = 0
    else:
        num_item = int(num_item) # Casting
    
    for item in range(num_item):
        item = input(f'Insira um valor qualquer {item + 1}: ').capitalize()
        # Validando a entrada para que não seja inseeridos valores vazios
        if ((item == '') or not (item.isalpha())):
            print('Valor Inválido')
        else:
            # Adicionando os itens ao set
            valores_set.add(item)
    
    os.system('cls')
    print('Item(ns) presentes no conjunto:')
    print('-' * 70)
    # Exibindo os valores presentes na lista
    if (len(valores_set) == 0): # Caso não possua nenhum valor
        print('Insira itens a lista.')
    for item in valores_set:
        print(item, end= ' | ')
    
    
    # Removendo
    print()
    print()
    # SElecionando o valor para ser removido e validando a entrada
    remover = input('Qual item você deseja remover? ').capitalize().strip()
    # Caso não exista valores no conjunto nada será removido
    if ((remover == ' ') or (remover not in valores_set)):
        print('Valor inválido! Tente novamente.')
    else:
        valores_set.remove(remover)
    
    os.system('cls')
    # Exibindo os itens presentes no conjunto após a exclusão
    print('Item(ns) presentes no conjunto após remove() ser aplicado.')
    print('-' * 70)
    if (len(valores_set) == 0): # Caso não possua nenhum valor
        print('Não há itens na lista.')
    for item in valores_set:
        print(item, end= ' | ')
    
    print()
    print()
    # Encerra ou não o sistema
    continua = input('Deseja encerrar o programa? (s/n): ').lower().strip()
    if continua == 's':
        os.system('cls')
        break
    else:
        os.system('cls')