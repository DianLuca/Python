import os


os.system('cls')
# Lista de dicionários
estoque = [
    {"produto": "Camiseta", "quantidade": 50, "preco_unitario": 25.99},
    {"produto": "Calça", "quantidade": 30, "preco_unitario": 39.99},
    {"produto": "Blusa", "quantidade": 20, "preco_unitario": 19.99},
    {"produto": "Calça Jeans", "quantidade": 35, "preco_unitario": 45.99},
    {"produto": "Alça Jeans", "quantidade": 30, "preco_unitario": 39.99}
]

# sorted pega a lista e retorna ordenada de acordo com o que foi solicitado
estoque = sorted(estoque, key=lambda x: x['produto'])
# Ordenando - Criar após uma forma de escolher como será filtrado - produto, quantidade e preço
while True: # Escolha de Ação
    filtro_busca = input('O que deseja realizar: FILTRO || BUSCA ').lower().strip()
    if filtro_busca == 'f':
        
        filtro = input(
        'Filtrar por: 1 - Produto | 2 - Quantidade | 3 - Preço | ').lower().strip()
        if filtro == '1' or filtro == 'produto':
            filtro = 'produto'
        elif filtro == '2' or filtro == 'quantidade':
            filtro = 'quantidade'
        elif filtro == '3' or filtro == 'preço':
            filtro = 'preco_unitario'
        else:  # Caso não seja definido nenhum ou algo diferente este será o padrão do sistema
            filtro = 'produto'

        # lambda pega a lista completa e difine X para usar como argumento, permitindo filtrar pelo que foi solicitado
        for item in estoque:
            print(f'Nome do produto: {item["produto"]} | '
                f'Quantidade: {item["quantidade"]} | '
                f'Valor: {item["preco_unitario"]}')
            
    else:
        while True:
            busca = input('Busca: ').strip()
            itens = 0

            encontrado = False  # Variável para controlar se o item foi encontrado

            # Verifica se os valores associados à chave "produto" começam com o prefixo especificado
            for item in estoque:
                # Usamos lower() para tornar a comparação insensível a maiúsculas e minúsculas
                if busca.lower() in item["produto"].lower():
                    print(f'Nome do produto: {item["produto"]} | '
                    f'Quantidade: {item["quantidade"]} | '
                    f'Valor: {item["preco_unitario"]}')
                    encontrado = True
            if not encontrado or busca == '':
                resposta_erro = f'Nenhum item "{busca}" encontrado com essa palavra nos nomes dos produtos.'
                print(resposta_erro.upper())    
                nova_busca = input('Deseja fazer uma nova busca? ')
                if nova_busca != 's':
                    os.system('cls')
                    break
# Para o caso de muitos itens devo procurar outras formas, essa busca é limitada
