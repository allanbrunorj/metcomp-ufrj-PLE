import numpy as np
''' Notação do arquivo:
    f: representa o objeto da função passada
    a: valor inicial do intervalo
    b: valor final do intervalo
    k: número de divisões no eixo x
'''


def integral_trapezio(f, a, b, k):
    '''Função que calcula a integral pelo método do trapézio'''
    x = np.linspace(a, b, k + 1)
    x_zero, x_final, x = x[0], x[-1], x[1:-1]
    resultado = (b - a)/k * (f(x_zero) + f(x_final) + sum(f(x)))
    return resultado


def metodo_simpson(f, a, b, k):
    '''Função que calcula a integral pelo método de simpson'''
    assert k % 2 != 1, "k tem que ser par"
    x = np.linspace(a, b, k + 1)
    split_1, split_2, split_3 = x[0:-1:2], x[1::2], x[2::2]
    resultado = (b - a)/(k * 3) * np.sum(f(split_1) + 4*f(split_2) + f(split_3))
    return resultado


def encontrar_k_necessario(metodo, f, limite_inicial, limite_final, precisao=10e-6):
    '''Encontra o mínimo K e o valor da integral para dada precisão.'''
    if metodo == metodo_simpson:
        k, step = 2, 2
    else:
        k, step = 1, 1
    valor_previo = metodo(f, limite_inicial, limite_final, k)
    while True:
        k += step
        valor_k = metodo(f, limite_inicial, limite_final, k)
        if abs(valor_k - valor_previo) < precisao:
            break
        valor_previo = valor_k

    return k, valor_k


def f_1(x): return np.sin(x)
def f_2(x): return 1/np.sqrt(2*np.pi) * np.exp(-x**2/2)  # De -2 a 2


limite_inicial, limite_final = -2, 2

k_trapezio, resultado_trapezio = encontrar_k_necessario(integral_trapezio, f_2,
                                                        limite_inicial,
                                                        limite_final)
k_simpson, resultado_simpson = encontrar_k_necessario(metodo_simpson, f_2,
                                                      limite_inicial,
                                                      limite_final)
print(f'Método   Valor da integral   k necessário')
print(f'-----------------------------------------')
print(f'Trapézio   {resultado_trapezio}   {k_trapezio}')
print(f'Simpson   {resultado_simpson}   {k_simpson}')
print('''Para otimizar o tempo de cálculo da integral, uma boa medida
é calcular a integral do início ao meio, e depois dobrar o resultado.
Diminuiria o tamanho de todas as arrays geradas nos cálculos pela metade.''')
