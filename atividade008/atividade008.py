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
    print('Utilizando o método REMOVE()')
    # Adicionando valores a lista
    num_item = input('Quantos itens deseja inserir? ').strip()
    if num_item == '' or not num_item.isnumeric():
        num_item = 0
    else:
        num_item = int(num_item)
    
    for item in range(num_item):
        item = input(f'Insira a fruta {item + 1}: ').capitalize()
        frutas_set.add(item)
        
    os.system('cls')
    print(frutas_set)
    
    # Removendo
    remover = input('Qual item você deseja remover? ').capitalize().strip()
    frutas_set.remove(remover)
    
    for item in frutas_set:
        print(item, end=' ')
    
    continua = input('Deseja encerrar o programa? (s/n): ').lower().strip()
    if continua == 's':
        os.system()
        break
    else:
        os.system()