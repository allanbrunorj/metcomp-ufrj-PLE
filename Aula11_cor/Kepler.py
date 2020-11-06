'''
O programa roda mas não fornece os resultados esperados.
Erro 1: Os passos estão incorretos. Eles deveriam ser n=365, n=24*365 e n=60*24*365 para, respectivamente, 1 dia, 1 hora e 1 minuto no Método de Euler.
Erro 2: O passo para o Método de Runge Kutta está incorreto. Deveriamos ter n=365.
Obs 1: As perguntas da Q.3 não foram respondidas.
Obs 2: A Q.4c não foi respondida.
'''

import matplotlib.pyplot as plt
import numpy as np

M = 1.98e30
G = 6.67e-11

ti = 0
tf = 31536000
ri = np.array([1.496e11, 0, 0, 2.97e4])
n = 86400 # dia
# n = 3600# hora
# n = 60# minuto

def derivada(r, t):
    '''Função que calcula a derivada do exercício
    e retorna uma array com x, dx, y, dy'''
    x = r[0]
    y = r[2]
    dx = -G * M * x/np.sqrt(x**2 + y**2)**3
    dy = -G * M * y/np.sqrt(x**2 + y**2)**3
    return np.array([r[1], dx, r[3], dy])

def Euler(f, ri, ti, tf, n):
    '''Função que calcula EDO de primeiro ordem de maneira numérica
    através do método de Euler.
    '''
    t = np.zeros(n)
    if isinstance(ri,(float, int)):
        r = np.zeros(n)
    else:
        r = np.zeros((n, len(ri)))

    t[0] = ti
    r[0] = ri
    h = (tf-ti)/n
    for k in range(n - 1):
        t[k + 1] = t[k] + h
        r[k + 1] = r[k]+h*f(r[k], t[k])
    return t, r

#------------- PLOTS EULER ---------------------
# t, r = Euler(derivada, ri, ti, tf, n)
# print (f"x = {x} e o t é {t}")
# plt.plot(r[:,0], r[:,2])
# plt.title('Órbita calculada com Minutos')
# plt.xlabel('Posição x')
# plt.ylabel('Posição y')
# plt.savefig('kepler_dia.png')
# plt.savefig('kepler_hora.png')
# plt.savefig('kepler_minuto.png')

#------------- PLOTS RUNGEKUTTA -----------
import rk4

r, t = rk4.RungeKutta4(derivada, ri, ti, tf, n)
plt.plot(r[:,0], r[:,2])
# plt.title('Órbita calculada com RungeKutta')
plt.xlabel('Posição x')
plt.ylabel('Posição y')
plt.show()
