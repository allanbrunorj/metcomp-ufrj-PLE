'''

não imprimiu o valor do próximo termo da série
[linha 50]- Erro está calculado errado
grafico está com o nome dos eixos errados
5/6
'''
# Dupla: Allan Bruno(IFA) e Lorena Dias(IFB)
import math
import matplotlib.pyplot as plt
import numpy as np

x = float(input('Quer o seno de que número? ')) #Valor para calcular o seno
n = int(input('Quantas iteraçoes? ')) #Número de iterações

def seno(valor, iteracoes):
	'''Função que calcula o seno através da série de Taylor'''
	seno_calculado = 0
	for n in range(iteracoes):
		seno_calculado += ((-1)**n * valor**(2*n+1))/math.factorial(2*n + 1)

	return seno_calculado

seno_taylor = seno(x, n) # Calculando o seno com n iterações
seno_real = math.sin(x) #Seno do math
diferenca_soma = seno_taylor - seno_real # Diferença dos dois senos
print('------------ LETRA A --------------')
print(f'Seno da soma: {seno_taylor}')
print(f'Seno do math: {seno_real}')
print(f'Diferença dos dois: {diferenca_soma}')

print('--------- LETRA B ------------')
'''Exemplos de cálculo de seno com diferentes quantidades
de iteração.'''
print(f'seno de pi')
print(f'n = 2: {seno(math.pi, 2)}')
print(f'n = 4: {seno(math.pi, 4)}')
print(f'n = 8: {seno(math.pi, 8)}')

print(f'seno de pi/4')
print(f'n = 2: {seno(math.pi/4, 2)}')
print(f'n = 4: {seno(math.pi/4, 4)}')
print(f'n = 8: {seno(math.pi/4, 8)}')

print('----------- LETRA C ----------')
x = math.pi/2
print(f'Seno de {x}.')
seno_real = math.sin(x)

for n in range(1, 6): # 2, 4, 6, 8, 10
	seno_calculado = seno(x, n)
	erro_seno = (seno_calculado - seno_real)**(n+1)
	print(f'Erro calculado: {erro_seno}. Valor de n -> {n}')


print(f'----------- LETRA D --------------')
'''Plots dos eixos para a serie de taylor com diferentes valores de n'''
eixo_x = np.arange(0, 3*math.pi/2, 0.1) #0, 0.1 0.2 0.3

eixo_y_real = np.sin(eixo_x)
plt.plot(eixo_x, eixo_y_real, label='np.sin(x)')#Plot Série de taylor - seno do numpy.

eixo_y_2 = [seno(x, 2) for x in eixo_x]
plt.plot(eixo_x, eixo_y_2, label='n = 2')#Plot Série de taylor com 2 iterações.

eixo_y_3 = [seno(x, 3) for x in eixo_x]
plt.plot(eixo_x, eixo_y_3, label='n = 3')#Plot Série de taylor com 3 iterações.

eixo_y_4 = [seno(x, 4) for x in eixo_x]
plt.plot(eixo_x, eixo_y_4, label='n = 4')#Plot Série de taylor com 4 iterações.

eixo_y_5 = [seno(x, 5) for x in eixo_x]
plt.plot(eixo_x, eixo_y_5, label='n = 5')#Plot Série de taylor com 5 iterações.

plt.ylim(-2, 2)
plt.title('Gráfico do Seno')
plt.ylabel('Graus')
plt.xlabel('x(graus)')
plt.legend(loc='lower left')
plt.show()
