# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# DESAFIO: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
import os


os.system('cls')

inicio = input('Deseja iniciar o sistema?[S - Sim] ').strip().lower()
os.system('cls')
# LISTA COM A CARTA DE VINHOS: TIPO DO VINHO, PAÍS, DESCRIÇÃO E PREÇO
carta_vinho = [{'categoria': 'Tinto', 'pais': 'Brasil', 'preco': 25.99,
                'descricao': 'Vinho com baixo teor alcoólico'},
               {'categoria': 'Tinto', 'pais': 'Nova Zelândia', 'preco': 25.99,
                'descricao': 'Vinho com baixo teor alcoólico'}
               ]

while inicio == 's':
    print('-' * 40 + '| ADEGA |' + '-' * 40)
    if len(carta_vinho) <= 0:
            print('FAVOR ADICIONAR ITEM(NS) À LISTA')
    # PARA LER: UTILIZAR FOR E PRINT(f'') - SAÍDA FORMATADA
    # APRESENTANDO TODOS OS ITENS NA TELA
    for i, item in enumerate(carta_vinho, start=1):
            print(f'{i}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço:R$ '
              + f'{item["preco"]:.2f} | Descrição: {item["descricao"]}')

    # OPÇÃO PARA ENTRAR NA CRUD
    print('-' * 35 + '| MENU DE OPÇÕES |' + '-' * 35)
    print('SELECIONE UMA DAS OPÇÕES:')
    opcoes = input('1 - ADICIONAR ITEM | 2 - ALTERAR ITEM | 3 - EXCLUIR ITEM | : ')
    
    ######################     CREATE     ########################
    if opcoes == '1':
        # Solicita ao usuário quantos vinhos deseja inserir
        print()
        num_vinhos = int(input('Quantos vinhos deseja inserir? '))
        os.system('cls')
        # Loop para inserir os dados de cada vinho e adicioná-los à lista
        for i in range(1, num_vinhos + 1):  
            print(f'Inserindo dados do vinho {i}:')
            categoria = input('Categoria: ').capitalize()
            pais = input('País: ').capitalize()
            preco = input('Preço(R$): ').replace(',', '.')
            if preco == '' or not preco.isdigit():
                preco = 0.0
            else:
                preco = float(preco)
            descricao = input('Descrição (Marca, Teor Alcoólico e outros): ').capitalize()
            os.system('cls')

            novo_item = [] 
            # Cria um dicionário com os dados inseridos e adiciona à lista_de_vinhos
            vinho = {'categoria': categoria, 'pais': pais,
                    'preco': preco, 'descricao': descricao}
            novo_item.append(vinho)  # Salva o item na lista novo_item

            # Envia os itens para a lista carta_vinho
            carta_vinho.extend(novo_item)

    ######################     UPDATE     ########################
    elif opcoes == '2':
        print()
        os.system('cls')
        while True:
            for item in carta_vinho:
                indice = carta_vinho.index(item) + 1
                #EXIBINDO A LISTA DE ITENS
                print(f'{indice}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço:R$ '
                    + f'{item["preco"]:.2f} | Descrição: {item["descricao"]}') 
            
            print()
            item_index = input('Qual deseja alterar (Selecione pelo número na tabela)? ')
            if item_index == '':
                print('Selecione novamente')
                item_index = input('Qual deseja alterar (Vazio retorna ao menu)? ')
                if item_index == '':
                    os.system('cls')
                    break
                else:
                    item_index = int(item_index) - 1
                    
            item_index = int(item_index) - 1
            
            # item_index = int(item_index) - 1
            # ALTERANDO OS ITENS DE ACORDO COM A LISTA
            print('Faça as alterações - FAVOR PREENCHER TODOS OS CAMPOS') # O não preenchimento torna o campo vazio
            categoria = input('Categoria: ').capitalize()
            pais = input('País: ').capitalize()
            preco = input('Preço(R$): ').replace(',', '.')
            if preco == '' or not preco.isdigit(): # Validando a entrada e convertendo para float
                preco = 0.0
            else:
                preco = float(preco)
            descricao = input('Descrição (Marca, Teor Alcoólico e outros): ').capitalize()
            os.system('cls')
            # RETORNANDO A ALTERAÇÃO PARA LISTA
            carta_vinho[item_index] = vinho = {'categoria': categoria, 'pais': pais,
                    'preco': preco, 'descricao': descricao}
        
            para_alteracao = input('Deseja alterar mais algum item?[S - Sim] ').strip().lower()
            if para_alteracao != 's':
                os.system('cls')
                break
            
            
    ######################     DELETE     ########################
    elif opcoes == '3':
        print()
        os.system('cls')
        while True:
            for item in carta_vinho:
                indice = carta_vinho.index(item)
                print(f'{indice + 1}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço:R$ '
                        + f'{item["preco"]:.2f} | Descrição: {item["descricao"]}')
            
            print()
            apagar = input('Número do item que deseja excluir? ') # Selecionando item pelo índice
            if apagar == '' or not apagar.isdigit(): # Validando a entrada
                print('Valor inválido! Tente Novamente')
                apagar = input('Número do item que deseja excluir? ')
                if apagar == '' or not apagar.isdigit():
                    os.system('cls')
                    break
            apagar = int(apagar) - 1
            removido = carta_vinho.pop(apagar)
            para_apagar = input('Deseja excluir mais algum item?[S - Sim]').strip().lower()
            if para_apagar != 's':
                os.system('cls')
                break
            else:
                os.system('cls')
    #########################################
    else:
        os.system('cls')
        parada = input('Deseja encerrar o programa?[S - Sim] ').strip().lower()
        os.system('cls')
        if parada == 's':
            saida = input('\u26A0\ufe0f  ATENÇÃO: INFELIZMENTE, AINDA NÃO É POSSÍVEL SALVAR OS DADOS INSERIDOS NESSE SISTEMA. REALMENTE DESEJA ENCERRAR?[S - Sim] ').strip().lower()
            if saida == 's':
                break
            else:
                os.system('cls')
else:
    os.system('cls')
    print('Programa encerrado!')
