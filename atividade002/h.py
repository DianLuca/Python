# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Dian Luca Valente Nascimento
# Data: 26/04/2024
# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes
# de equações quadráticas para auxiliar engenheiros e cientistas em suas 
# análises e projetos. Eles precisam de um programa que calcule as raízes da 
# equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, 
# utilizando apenas os conceitos e operações básicas aprendidos até o momento. 
# Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser 
# capaz de calcular essas raízes de forma precisa, seguindo os princípios 
# matemáticos fundamentais.

# Import
import os


os.system('cls')

# Declarações
# 𝑥²−6𝑥+5 onde a = 1, b = -6 c =6
raiz_quadrada = 1/2
x1 = 5
x2 = 1

# Processamento
calculo_5 = (x1**2 - 6*x1 + 5) ** raiz_quadrada
calculo_1 = (x2**2 - 6*x2 + 5) ** raiz_quadrada
# outro_calculo = (x1**2 - 6*x2 + 5) ** raiz_quadrada

# Saída
print(f'{calculo_5:.2f} e {calculo_1:.2f}')
# print(outro_calculo)