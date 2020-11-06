'''
Sem erros

Poderia acrescentar comentarios
exemplo:#essse programa calcula o valor de pi usando numeros aleatorio, #importando variaveis, #calculando valorda funcao, #calculando o somantorio, etc
Sandra: 3.5
'''
from math import sqrt, pi, exp
m = 0
s = 2.
x = 1.
gaussiana = 1/(s*sqrt(2*pi))*exp(-1/2.*((x-m)/s)**2)
print(gaussiana)
