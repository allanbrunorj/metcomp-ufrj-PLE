'''
O programa roda e fornece os resultados esperados.
Obs 1: Cuidado com chutes iniciais excessivamente longe do valor da raiz. Isso pode gerar lentidão desnecessária no programa.
Observe o gráfico da função para decidir um chute inicial.
Obs 2: Não foi imposto um limite para a quantidade de iterações. Isso pode gerar lentidão no programa dependendo dos
intervalos utilizados e no caso em que há baixa taxa de variação da equação próximo da raiz.
Obs 3: Foram importadas bibliotecas que não foram utilizadas
Obs 4: Programa sem comentários.
Obs 5:  Cuidado com divisões por zero. Caso o valor do chute inicial seja 0 ou 1.5e11 teriamos uma divisão por zero
na função e sua derivada.
'''

#Allan Bruno(IFA) e Lorena Dias(IFB)
import numpy as np

def NR(f,f_linha, chute_inicial, precisao):
    x_n = chute_inicial
    n_iteracoes = 0
    while True:
        n_iteracoes += 1
        x_n_1 = x_n - f(x_n)/f_linha(x_n)
        if abs(x_n_1 - x_n) < precisao:
            break
        x_n = x_n_1
    print(f'O raio é {x_n_1} com {n_iteracoes} iterações')

G = 6.674e-11
M = 1.989e30
m = 5.9736e24
R = 1.5e11
w = 1.992e-7

f = lambda r: G*M/r**2 - G*m/(R-r)**2 - r*w**2
f_linha = lambda r: -2*G*M/r**3 - 2*G*m/(R-r)**3 - w**2
chute_inicial = 5
precisao = 1e-5
NR(f, f_linha, chute_inicial, precisao)
