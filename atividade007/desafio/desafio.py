# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# DESAFIO: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
import os
import tabulate


os.system('cls')

inicio = input('Deseja iniciar o sistema?[S - Sim] ').strip().lower()
os.system('cls')
# LISTA COM A CARTA DE VINHOS: TIPO DO VINHO, PAÍS, DESCRIÇÃO E PREÇO
# CÓDIGO PARA COMPILAR python -m py_compile desafio.py

carta_vinho = [  # EXEMPLO DE COMO DEVE SER:
    {'categoria': 'Tinto', 'pais': 'Brasil', 'preco': 25.99, 'descricao': 'Marca: Miolo Wine Group. '
     'Este vinho apresenta-se equilibrado, redondo com final de boca agradável.'}
]

while inicio == 's':
    print('-' * 40 + '| ADEGA |' + '-' * 40)
    print('-' * 36 + '| MENU DE OPÇÕES |' + '-' * 35)
    # OPÇÃO PARA ENTRAR NA CRUD
    opcoes = input(
        '1 - EXIBIR APENAS A LISTA | 2 - ADICIONAR ITEM | 3 - ALTERAR ITEM '
         + '| 4 - EXCLUIR ITEM | : ').strip()

    if opcoes == '1':
        os.system('cls')
        while True:
            print('-' * 65 + '| ADEGA |' + '-' * 65)
            if len(carta_vinho) <= 0:
                print()
                print('FAVOR ADICIONAR ITEM(NS) À LISTA')
                print()
            # for i, item in enumerate(carta_vinho, start=1):
            #     print(f'{i}| Categoria: {item["categoria"]} | '
            #           + f'País: {item["pais"]} | '
            #           + f'Preço:R$ {item["preco"]:.2f} | '
            #           + f'Descrição: {item["descricao"]}')
            carta_vinho = [{**{'':i + 1}, **row} for i, row in enumerate(carta_vinho)]
            print(tabulate.tabulate(carta_vinho, headers= 'keys', tablefmt= 
                        'rounded_grid', showindex= 'num', stralign='center'))
            print('=' * 70)
            volta_menu = input('Deseja voltar ao menu?[S - Sim] ')
            os.system('cls')
            if volta_menu == 's':
                os.system('cls')
                break

    # PARA LER: UTILIZAR FOR E PRINT(f'') - SAÍDA FORMATADA
    # APRESENTANDO TODOS OS ITENS NA TELA
    ######################      READ       ########################

    ######################     CREATE     ########################
    elif opcoes == '2':
        while True:  # SOLICITA AO USUÁRIO QUANTOS VINHOS DESEJA INSERIR
            print()
            num_vinhos = input('Quantos vinhos deseja inserir (Campo vazio '
                               + 'ou letras não são aceitos)? ')
            if (num_vinhos == '' or not num_vinhos.isnumeric()):
                num_vinhos = 0

            num_vinhos = int(num_vinhos)
            os.system('cls')
        # LOOP PARA INSERIR OS DADOS DE CADA VINHO E ADICIONÁ-LOS À LISTA
            for i in range(1, num_vinhos + 1):
                print(f'Inserindo dados do vinho {i}:')
                categoria = input(
                    'Categoria (Ex.:Rosê, Tinto): ').capitalize().strip()
                pais = input('País (Ex.: Brasil): ').capitalize().strip()
                preco = input('Preço(R$): ').replace(',', '.').strip()
                if preco == '':  # CONVERTENDO E VALIDANDO A ENTRADA
                    preco = 0.0
                elif preco.replace('.', '', 1).isdigit():
                    preco = float(preco)
                else:
                    preco = 0.0
                descricao = input(
                    'Descrição (Marca, Teor Alcoólico ' 
                    + 'e outros): ').capitalize().strip()
                os.system('cls')

                novo_item = []
                # CRIA UMA VARIÁVEL PARA RECEBER TODOS OS DADOS
                vinho = {'categoria': categoria, 'pais': pais,
                         'preco': preco, 'descricao': descricao}
                novo_item.append(vinho)  # SALVA O ITEM NA LISTA novo_item

            # ENVIA OS ITENS PARA carta_vinho
                carta_vinho.extend(novo_item)

            para_adicionar = input(
                'Deseja adicionar mais algum item?[S - Sim] ').strip().lower()
            if para_adicionar != 's':
                os.system('cls')
                break
            else:
                os.system('cls')

    ######################     UPDATE     ########################
    elif opcoes == '3':
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
                'Qual deseja alterar (Selecione pelo número na '
                + 'tabela)? ').strip()
            if (item_index == '' or not item_index.isnumeric()):
                print('Selecione novamente')
                item_index = input(
                    'Qual deseja alterar (Vazio retorna ao menu)? ').strip()
                if item_index == '' or not item_index.isnumeric():
                    os.system('cls')
                    break
            else:
                item_index = int(item_index) - 1

            item_index = int(item_index) - 1

            # ALTERANDO OS ITENS DE ACORDO COM A LISTA
            # O NÃO PREENCHER TORNA O CAMPO VAZIO
            print('Faça as alterações - FAVOR PREENCHER TODOS OS CAMPOS')
            categoria = input(
                'Categoria (Ex.:Rosê, Tinto): ').capitalize().strip()
            pais = input('País (Ex.: Brasil): ').capitalize().strip()
            preco = input('Preço(R$): ').replace(',', '.').strip()
            if preco == '':
                preco = 0.0
            elif preco.replace('.', '', 1).isdigit():
                preco = float(preco)
            else:
                preco = 0.0
            descricao = input(
                'Descrição (Marca, Teor Alcoólico e '
                + 'outros): ').capitalize().strip()
            os.system('cls')
            # RETORNANDO A ALTERAÇÃO PARA LISTA
            carta_vinho[item_index] = vinho = {'categoria': categoria,
                                               'pais': pais, 'preco': preco, 
                                               'descricao': descricao}

            para_alteracao = input(
                'Deseja alterar mais algum item?[S - Sim] ').strip().lower()
            if para_alteracao != 's':
                os.system('cls')
                break

    ######################     DELETE     ########################
    elif opcoes == '4':
        print()
        os.system('cls')
        while True:
            for item in carta_vinho:
                indice = carta_vinho.index(item) + 1
                print(f'{indice}| Categoria: {item["categoria"]} | '
                      + f'País: {item["pais"]} | Preço:R$ '
                      + f'{item["preco"]:.2f} | Descrição: '
                      + f'{item["descricao"]}')

            print()
            # SELECIONANDO ITEM PELO INDÍCE
            apagar = input('Número do item que deseja excluir? ').strip()
            if apagar == '' or not apagar.isnumeric():  # VALIDANDO A ENTRADA
                print('Valor inválido! Tente Novamente')
                apagar = input('Número do item que deseja excluir? ').strip()
                if apagar == '' or not apagar.isnumeric():
                    os.system('cls')
                    break
                
            apagar = int(apagar) - 1
            if ((0 <= int(apagar) > len(carta_vinho)) or (len(carta_vinho) <= 0)):
                print()
                erro_excluir = input('O valor inserido não está na lista. Precione enter para continuar. ')
                if erro_excluir == '':
                    os.system('cls')
                    break
            removido = carta_vinho.pop(apagar)
            para_apagar = input(
                'Deseja excluir mais algum item?[S - Sim] ').strip().lower()
            if para_apagar != 's':
                os.system('cls')
                break
            else:
                os.system('cls')
    #########################################
    else:
        os.system('cls')
        print('Nenhum dos valores foi selecionado!')
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
