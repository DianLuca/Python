import os
import time


os.system('cls')
# Criação do dicionário vazio
meu_dicionario = {}

while True:
    os.system('cls')
    print('-' * 70)
    # Exibição do menu de opções
    print('\nMenu de opções:')
    print('1 - Adicionar um par chave-valor')
    print('2 - Mostra o dicionário')
    print('3 - Mostrar o tamanho do dicionário')
    print('4 - Fazer uma cópia do dicionário')
    print('5 - Limpar o dicionário')
    print('6 - Sair')
    print('-' * 70)
    
    # Solicitação da escolha do usuário
    opcao = input('Escolha um opção (1-6): ')
    
    os.system('cls')
    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionando.')
    elif opcao == '2':
        # Exibe o dicionário atual
        print('Dicionário atual:', meu_dicionario)
        time.sleep(4)
        
    elif opcao == '3':
        # Mostra o tamanho do dicionário usando len()
        tamanho = len(meu_dicionario)
        print(f'O dicionário tem {tamanho} elementos.')
        
    elif opcao == '4':
        # Cria uma cópia do dicionário usando copy() e exibe a cópia
        copia_dicionario = meu_dicionario.copy()
        print('Cópia do dicionário:', copia_dicionario)
        
    elif opcao == '5':
        # Limpa o dicionário usando clear()
        meu_dicionario.clear()
        print('Dicionário limpo.')
        
    elif opcao == '6':
        print('Saindo do programa.')
        break
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')