'''
Gabriella
 -sem erros
OBS: o programa itera uma vez a mais do que o declarado
'''

import math #importando modulo math
#Definindo variáveis
x = 1.2 
n = 5
print(f'Vamos calcular o seno de {x}')
print(f'Valor do seno(n de iterações da série): {n}')
print(f'Seno do módulo math: {math.sin(x)}') #Print do math.sin pra comparar com o valor da série
seno = 0 # Definindo a variável seno
for n in range(n+1): #Como o ultimo valor é excludente, adicionamos +1
	seno += ((-1)**n/math.factorial(2*n+1))*x**(2*n+1) #algoritmo da série

print(f'Seno implementado: {seno}') #Print do seno calculado pela série
