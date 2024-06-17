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
carta_vinho = [# EXEMPLO DE COMO DEVE SER:
    #{'categoria': 'Tinto', 'pais': 'Brasil', 'preco': 25.99,'descricao': 'Marca: Miolo Wine Group, 
    # Este vinho apresenta-se equilibrado, redondo com final de boca agradável.'},
               ]

while inicio == 's':
    print('-' * 40 + '| ADEGA |' + '-' * 40)
    print()
    if len(carta_vinho) <= 0:
        print('FAVOR ADICIONAR ITEM(NS) À LISTA')
    # PARA LER: UTILIZAR FOR E PRINT(f'') - SAÍDA FORMATADA
    # APRESENTANDO TODOS OS ITENS NA TELA
    for i, item in enumerate(carta_vinho, start=1):
        print(f'{i}| Categoria: {item["categoria"]} | País: {item["pais"]} |'
              + f' Preço:R$ {item["preco"]:.2f} | ' 
              + f'Descrição: {item["descricao"]}')

    # OPÇÃO PARA ENTRAR NA CRUD
    print()
    print('-' * 35 + '| MENU DE OPÇÕES |' + '-' * 35)
    print('SELECIONE UMA DAS OPÇÕES:')
    opcoes = input(
        '1 - ADICIONAR ITEM | 2 - ALTERAR ITEM | 3 - EXCLUIR ITEM | : ')

    ######################     CREATE     ########################
    if opcoes == '1':
        # SOLICITA AO USUÁRIO QUANTOS VINHOS DESEJA INSERIR
        print()
        num_vinhos = int(input('Quantos vinhos deseja inserir? '))
        os.system('cls')
        # LOOP PARA INSERIR OS DADOS DE CADA VINHO E ADICIONÁ-LOS À LISTA
        for i in range(1, num_vinhos + 1):
            print(f'Inserindo dados do vinho {i}:')
            categoria = input('Categoria (Ex.:Rosê, Tinto): ').capitalize()
            pais = input('País (Ex.: Brasil): ').capitalize()
            preco = input('Preço(R$): ').replace(',', '.')
            if preco == '' or not preco.isdigit():
                preco = 0.0
            else:
                preco = float(preco)
            descricao = input(
                'Descrição (Marca, Teor Alcoólico e outros): ').capitalize()
            os.system('cls')

            novo_item = []
            # CRIA UMA VARIÁVEL PARA RECEBER TODOS OS DADOS
            vinho = {'categoria': categoria, 'pais': pais,
                     'preco': preco, 'descricao': descricao}
            novo_item.append(vinho)  # SALVA O ITEM NA LISTA novo_item

            # ENVIA OS ITENS PARA carta_vinho 
            carta_vinho.extend(novo_item)

    ######################     UPDATE     ########################
    elif opcoes == '2':
        print()
        os.system('cls')
        while True:
            for item in carta_vinho:
                indice = carta_vinho.index(item) + 1
                # EXIBINDO A LISTA DE ITENS
                print(f'{indice}| Categoria: {item["categoria"]} | '
                      + f'País: {item["pais"]} | Preço:R$ '
                      + f'{item["preco"]:.2f} | Descrição: '
                      + f'{item["descricao"]}')

            print()
            item_index = input(
                'Qual deseja alterar (Selecione pelo número na tabela)? ')
            if item_index == '':
                print('Selecione novamente')
                item_index = input(
                    'Qual deseja alterar (Vazio retorna ao menu)? ')
                if item_index == '':
                    os.system('cls')
                    break
                else:
                    item_index = int(item_index) - 1

            item_index = int(item_index) - 1

            # ALTERANDO OS ITENS DE ACORDO COM A LISTA
            # O NÃO PREENCHER TORNA O CAMPO VAZIO
            print('Faça as alterações - FAVOR PREENCHER TODOS OS CAMPOS')
            categoria = input('Categoria (Ex.:Rosê, Tinto): ').capitalize()
            pais = input('País (Ex.: Brasil): ').capitalize()
            preco = input('Preço(R$): ').replace(',', '.')
            if preco == '' or not preco.isdigit():  # VALIDANDO A ENTRADA E REALIZANDO UM CASTING PARA FLOAT
                preco = 0.0
            else:
                preco = float(preco)
            descricao = input(
                'Descrição (Marca, Teor Alcoólico e outros): ').capitalize()
            os.system('cls')
            # RETORNANDO A ALTERAÇÃO PARA LISTA
            carta_vinho[item_index] = vinho = {'categoria': categoria, 
                        'pais': pais, 'preco': preco, 'descricao': descricao}

            para_alteracao = input(
                'Deseja alterar mais algum item?[S - Sim] ').strip().lower()
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
                print(f'{indice}| Categoria: {item["categoria"]} | '
                      + f'País: {item["pais"]} | Preço:R$ '
                      + f'{item["preco"]:.2f} | Descrição: '
                      + f'{item["descricao"]}')

            print()
            # SELECIONANDO ITEM PELO INDÍCE
            apagar = input('Número do item que deseja excluir? ')
            if apagar == '' or not apagar.isdigit():  # VALIDANDO A ENTRADA
                print('Valor inválido! Tente Novamente')
                apagar = input('Número do item que deseja excluir? ')
                if apagar == '' or not apagar.isdigit():
                    os.system('cls')
                    break
            apagar = int(apagar) - 1
            removido = carta_vinho.pop(apagar)
            para_apagar = input(
                'Deseja excluir mais algum item?[S - Sim]').strip().lower()
            if para_apagar != 's':
                os.system('cls')
                break
            else:
                os.system('cls')
    #########################################
    else:
        os.system('cls')
        parada = input('Deseja encerrar o programa?'
                       + f'[S - Sim] ').strip().lower()
        os.system('cls')
        if parada == 's':
            saida = input(
                '\u26A0\ufe0f  ATENÇÃO: INFELIZMENTE, AINDA NÃO É POSSÍVEL '
                + f'SALVAR OS \nDADOS INSERIDOS NESSE SISTEMA. REALMENTE ' 
                + f'DESEJA ENCERRAR?[S - Sim] ').strip().lower()
            if saida == 's':
                break
            else:
                os.system('cls')
else:
    os.system('cls')
    print('Programa encerrado!')
