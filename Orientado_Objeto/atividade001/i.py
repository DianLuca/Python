# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 03/09/2024
# Faça um programa que receba um valor em reais, depois calcule quantos
# dólares daria para comprar com esse valor.
import os


valor_dolar = 5.64  # Cotação de 03/09/2024


class Cambio:
    def __init__(self, moeda):
        self.moeda = moeda

    def conversor(self):
        try:
            moeda = float(self.moeda)
            conversao_dolar_real = valor_dolar * moeda
            conversao_real_dolar = moeda / valor_dolar
            return f'$ {moeda:.2f} dólar(es) corresponde a: R$ {conversao_dolar_real:.2f} \nR$ {moeda:.2f} real(is) correspondem a: $ {conversao_real_dolar:.2f}'
        
        except ZeroDivisionError:
            return 'Impossível realizar divisão por zero! '
            
        except (TypeError, ValueError):
            return 'Insira apenas valores numéricos! '


while True:
    os.system('cls')

    print('-' * 70)
    print('ENTRADA DE DADOS')
    print('-' * 70)

    # Entrada
    valor_real = input('Insira um valor em reais para conversão (s - Sair): ')
    if valor_real == 's':
        break
    else:
        cambio = Cambio(valor_real)
        valor_convertido = cambio.conversor()

    print('-' * 70)
    print('--- CONVERSÃO DE VALORES')
    input(f'{valor_convertido}\n' + '=' * 70)
