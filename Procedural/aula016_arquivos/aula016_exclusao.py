import csv
import os


os.system('cls')
arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'
nome_para_pagar = input('Digite o nome que deseja apagar: ')

# Lendo dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
# Verificando se o nome existe e apagando o registro
agagado = False
novo_cadastro = [registro for registro in cadastro if registro['nome'] != nome_para_pagar]

if len(novo_cadastro) < len(cadastro):
    apagado = True
    
# Reescrevendo o arquivo com dados atualizados
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['nome', 'telefone', 'cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(novo_cadastro)

print('-' * 70)
if apagado:
    print(f'Registro com o nome {nome_para_pagar} apagado com sucesso.')
else:
    print(f'Registro com o nome {nome_para_pagar} não encontrado.')
print('-' * 70)
    