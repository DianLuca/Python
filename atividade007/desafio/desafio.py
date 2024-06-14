# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 17/06/2024
# DESAFIO: Construa um código para exemplificar um CRUD. Não é permitido funções ou validações try exception.
import os


os.system('cls')

inicio = input('Deseja iniciar o sistema?[S - Sim] ').strip().lower()
    
# LISTA COM A CARTA DE VINHOS: TIPO DO VINHO, PAÍS, DESCRIÇÃO E PREÇO 
carta_vinho = [{'categoria': 'Tinto', 'pais': 'Brasil', 'preco': 25.99, 'descricao': 'Vinho com baixo teor alcoólico'},
                {'categoria': 'Tinto', 'pais': 'Nova Zelândia', 'preco': 25.99, 'descricao': 'Vinho com baixo teor alcoólico'}
]

while inicio == 's':
    print('-'* 35 + '| CARTA DE VINHOS |' + '-'* 35)
    
    for i, item in enumerate(carta_vinho, start= 1): # APRESENTANDO TODOS OS ITENS NA TELA
        print(f'{i}| Categoria: {item["categoria"]} | País: {item["pais"]} | Preço: {item["preco"]} | Descrição: {item["descricao"]}')
    
    
    # PARA INSERIR: UTILIZAR APPEND() OU EXTEND()
    # Inicializa uma lista vazia para armazenar os vinhos


    # Solicita ao usuário quantos vinhos deseja inserir
    print()
    num_vinhos = int(input("Quantos vinhos deseja inserir? "))

    # Loop para solicitar os dados de cada vinho e adicioná-los à lista
    for i in range(1, num_vinhos + 1):
        print(f"Inserindo dados do vinho {i}:")
        categoria = input("Categoria: ")
        pais = input("País: ")
        preco = float(input("Preço: ").replace(',','.'))
        descricao = input("Descrição: ")
    
        novo_item = []
        # Cria um dicionário com os dados inseridos e adiciona à lista_de_vinhos
        vinho = {'categoria': categoria, 'pais': pais, 'preco': preco, 'descricao': descricao}
        novo_item.append(vinho)

        carta_vinho.extend(novo_item)


    # PARA LER: UTILIZAR FOR E PRINT(f'') - SAÍDA FORMATADA

    # PARA ATUALIZAR: UTILIZAR INDEX() E SELECIONAR O ITEM

    # PARA APAGAR: UTILIZAR INDEX() POP()
    print()        
    saida = input('Deseja encerrar o programa?[S - Sim] ').strip().lower()
    if saida == 's':
        break
    else:
        os.system('cls')
else:
    os.system('cls')
    print('Programa encerrado!')