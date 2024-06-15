# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# DESAFIO: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
import os


os.system('cls')

inicio = input('Deseja iniciar o sistema?[S - Sim] ').strip().lower()

# LISTA COM A CARTA DE VINHOS: TIPO DO VINHO, PAÍS, DESCRIÇÃO E PREÇO
carta_vinho = [{'categoria': 'Tinto', 'pais': 'Brasil', 'preco': 25.99,
                'descricao': 'Vinho com baixo teor alcoólico'},
               {'categoria': 'Tinto', 'pais': 'Nova Zelândia', 'preco': 25.99,
                'descricao': 'Vinho com baixo teor alcoólico'}
               ]

while inicio == 's':
    print('-' * 35 + '| CARTA DE VINHOS |' + '-' * 35)
    # PARA LER: UTILIZAR FOR E PRINT(f'') - SAÍDA FORMATADA
    # APRESENTANDO TODOS OS ITENS NA TELA
    for i, item in enumerate(carta_vinho, start=1):
        print(f'{i}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço: '
              + f'{item["preco"]} | Descrição: {item["descricao"]}')

    # OPÇÃO PARA ENTRAR NA CRUD
    print('-' * 35 + '| MENU DE OPÇÕES |' + '-' * 35)
    print('SELECIONE UMA DAS OPÇÕES:')
    opcoes = input('1 - CRIAR NOVO ITEM | 2 - ALTERAR ITEM (Em desenvolvimento) | 3 - EXCLUIR ITEM |')
######################     CREATE     ########################
    if opcoes == '1':
        # PARA INSERIR: UTILIZAR APPEND() OU EXTEND()
        # Inicializa uma lista vazia para armazenar os vinhos

        # Solicita ao usuário quantos vinhos deseja inserir
        print()
        num_vinhos = int(input("Quantos vinhos deseja inserir? "))

        # Loop para solicitar os dados de cada vinho e adicioná-los à lista
        for i in range(1, num_vinhos + 1):  # Adiciona item a item na lista abaixo
            print(f"Inserindo dados do vinho {i}:")
            categoria = input("Categoria: ")
            pais = input("País: ")
            preco = float(input("Preço: ").replace(',', '.'))
            descricao = input("Descrição: ")
            os.system('cls')

            novo_item = []
            # Cria um dicionário com os dados inseridos e adiciona à lista_de_vinhos
            vinho = {'categoria': categoria, 'pais': pais,
                    'preco': preco, 'descricao': descricao}
            novo_item.append(vinho)  # Salva o item na lista novo_item

            # Envia os itens para a lista carta_vinho
            carta_vinho.extend(novo_item)

        # PARA ATUALIZAR: UTILIZAR INDEX() E SELECIONAR O ITEM
    elif opcoes == '2':
        print('EM DESENVOLVIMENTO')
        ############### DELETE ##############
    elif opcoes == '3':
        busca_apagar = input('Qual item deseja remover: ')
        os.system('cls')
        while True:
            for item in carta_vinho:
                if (busca_apagar not in item["categoria"]) and (busca_apagar not in item["pais"]):
                    print('Não existe nenhum item com essas caracteristicas na Carta de Vinhos')
                else:
                    indice = carta_vinho.index(item)
                    print(f'{indice + 1}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço: '
                        + f'{item["preco"]} | Descrição: {item["descricao"]}')
            
            apagar = int(input('Número do item que deseja excluir? '))
            apagar = apagar - 1
            removido = carta_vinho.pop(apagar)
            para_apagar = input('Deseja excluir mais algum item?[S - Sim]').strip().lower()
            if para_apagar != 's':
                break
#########################################
    else:
        saida = input('Deseja encerrar o programa?[S - Sim] ').strip().lower()
        if saida == 's':
            break
        else:
            os.system('cls')
else:
    os.system('cls')
    print('Programa encerrado!')
