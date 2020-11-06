#Allan Bruno(IFA) e Lorena Dias(IFB)
import math
import matplotlib.pyplot as plt
import numpy as np
def sinal(x: float) -> float:
    if x > 0:
        return 1
    if x < 0:
        return -1
def media(*valores):
    return sum(valores)/len(valores)

def bissecao(f, a: float, b: float, precisao: float) -> float:
    if f(a)*f(b) >= 0:
        return None
    n_iteracoes = 0
    p_menos_1 = media(a,b)-1e-8
    while True:
        p = media(a, b)
        if f(p) == 0:
            print(f'O p é {p}')
            return None
        if sinal(f(a)) == sinal(f(p)):
            a = p
        else:
            b = p
        n_iteracoes += 1
        if n_iteracoes > 1:
            if abs(f(p) - f(p_menos_1)) < precisao:
                break
        p_menos_1 = p
    print(f'Raiz encontrada com {n_iteracoes} iterações: {p}')

print("Para a primeira função:")
#A primeira raiz positiva está entre 0 e 1.2
funcao_1 = lambda x: np.exp(-x) - np.sin(np.pi*x/2)
a_1 = 0
b_1 = 1.2
precisao_1 = 1e-5
bissecao(funcao_1, a_1, b_1, precisao_1)
print("\nPara a segunda função:")
#A primeira raiz positiva está entre 5 e 10
a_2 = 5
b_2 = 7.5
funcao_2 = lambda x: np.sin(0.1*x**2 + 3) - (2/x)**(1/2)
precisao_2 = 1e-5
bissecao(funcao_2, a_2, b_2, precisao_2)
