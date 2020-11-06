#Allan Bruno(IFA)e Lorena Dias(IFB)
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
        print(f'{n_iteracoes} - {x_n_1}')
    print(f'A raiz é {x_n_1} com {n_iteracoes} iterações')

f = lambda x: np.exp(-x) - np.sin(np.pi*x/2)
f_linha = lambda x: -np.exp(-x) - np.pi*np.cos(np.pi*x/2)/2
chute_inicial = 0.6
precisao = 1e-7
NR(f, f_linha, chute_inicial, precisao)
