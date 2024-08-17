import csv
import os


# Passando os caminhos para os itens
pasta = 'testes_csv_modulo/arquivo_csv'
arquivo = 'arquivo_csv.csv'
caminho = os.path.join(pasta, arquivo)

# Cria a pasta se caso ela não existir
os.makedirs(pasta, exist_ok=True)

# Verificando se o arquivo existe
arquivo_existe = os.path.isfile(caminho)

def ler_arquivo():
    """ Função para ler o arquivo csv
    Args:
        caminho (_type_): Local de onde será solicitado as informações do arquivo
    Returns:
        _type_: será retornado uma lista com todos os valores contidos no arquivo
    """    
    with open(caminho, 'r') as arquivo_csv:
        ler = csv.DictReader(arquivo_csv, delimiter=';')
        return list(ler) # Retorna uma lista com os dados do arquivo
    
def escrever_arquivo(caminho, dados):
    """ Função para inserir valores ao arquivo

    Args:
        caminho (_type_): Local onde será escrito as informações
        dados (_type_): Valores que serão inseridos ao arquivo
    """    
    with open(caminho, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'idade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        escrever.writeheader()
        escrever.writerows(dados)

def adicionar_arquivo(dados):
    with open(caminho, 'a', newline='') as arquivo_csv:
        campos = ['nome', 'idade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        escrever.writerows(dados)
    
if not arquivo_existe: # Se o arquivo não existir escreve o arquivo
    with open(caminho, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'idade']
        escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        escrever.writeheader()

