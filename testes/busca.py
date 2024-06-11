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

# Ordenando - Criar após uma forma de escolher como será filtrado - produto, quantidade e preço
# os.system('cls')
filtro = input('Filtrar por: 1 - Produto | 2 - Quantidade | 3 - Preço | ').lower().strip()

if filtro == '1' or filtro == 'produto':
    filtro = 'produto'
elif filtro == '2' or filtro == 'quantidade':
    filtro = 'quantidade'
elif filtro == '3' or filtro == 'preço':
    filtro = 'preco_unitario'
else: # Caso não seja definido nenhum ou algo diferente este será o padrão do sistema
    filtro = 'produto'
    

lista_crescente = sorted(estoque, key=lambda x: x[filtro]) # sorted pega a lista e retorna ordenada de acordo com o que foi solicitado
for item in lista_crescente:                               # lambda pega a lista completa e difine X para usar como argumento, permitindo filtrar pelo que foi solicitado
    print(f'Nome do produto: {item["produto"]} | '
              f'Quantidade: {item["quantidade"]} | '
              f'Valor: {item["preco_unitario"]}')

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
if not encontrado:
    print('Nenhum item encontrado com essa palavra nos nomes dos produtos.')

# Para o caso de muitos itens devo procurar outras formas, essa busca é limitada
