import csv
import os


lista = [
    {'nome':'Agata','telefone':'(32)99196-0000','cidade':'Juiz de Fora'},
    {'nome':'Bia','telefone':'(32)99196-0000','cidade':'Juiz de Fora'},
    {'nome':'Coly','telefone':'(32)99196-0000','cidade':'Juiz de Fora'},
    {'nome':'Isis','telefone':'(32)99196-0000','cidade':'Juiz de Fora'}
]

# Caminho para a pasta onde o arquivo CSV será salvo
pasta = 'aula016_arquivos/arquivos_csv/gravacao/'

# Verificando se a pasta existe, se não, irá criá-la
os.makedirs(pasta, exist_ok=True)

# Nome para o arquivo CSV para gravar as informações
arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'

# Caminho completo do arquivo CSV
caminho_arquivo = os.path.join(pasta, arquivo)

# Abre o arquivo 'arquivo' no modo de escrita ('w'). 
# Se o arquivo não existir, ele será criado; se existir, será truncado (esvaziado). 
# newline='': Evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas. 
# as arquivo_csv: Atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # campos = ['name', 'telefone', 'cidade']: Define a lsita de nomes de campos
    # (cabeçalhos das colunas do CSV).
    campos = ['nome', 'telefone', 'cidade']
    
    # writer = csv.DictWriter(arquivo_csv, fieldnames=campos): 
    # Cria um objeto DictWriter que usará 'arquivo_csv' para gravar os campos. 
    # fieldnames define a ordem dos campos no arquivo CSV. 
    # delimiter=';': é o separador.
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    # writer.whiterheader(): Grava a linha de cabeçalho no
    # arquivo CSV usando os nomes de campos definidos em fieldnames.
    escrever.writeheader()
    
    # writer.writerows(lista): Grava todas as linhas da lista no arquivo CSV.
    # Cada dicionário em 'lista' se torna uma linhas no arquivo.
    escrever.writerows(lista)
    
os.system('cls')

print(f'Arquivo {arquivo} gravado com sucesso!')