import os


os.system('cls')

salario = float(input('Insira o seu salário atual: '))
resposta = ''

if salario <= 0:
    resposta = print(f'Insira um valor maior do que 0.')
elif salario >= 1500:
    salario_futuro = salario + (salario * 0.05) # 0.05 corresponde a 5%
    resposta = (f'Seu salário era de R$ {salario:.2f} e passará a ser' 
    + f'R$ {salario_futuro:.2f}')
elif salario <= 1000:
    salario_futuro = salario + (salario * 0.1) # 0.1 corresponde a 10%
    resposta = (f'Seu salário é R$ {salario:.2f} e passará a ser' 
    + f'R$ {salario_futuro:.2f}')
else:
    resposta = 'Seu salário não irá sofrer alteração'

print()
print(resposta)
print('-' * 70)