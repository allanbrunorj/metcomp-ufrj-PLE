'''
 - [linhas 29, 39 e 40] Os arrays de t e x (ou x e y aqui) deveriam
   começar com os valores iniciais de t e x.
       Caso a atribuição desses valores aos primeiros elementos dos
       arrays fosse feita antes do 'for', seria necessário mudar o
       loop 'for' para que os atuais últimos elementos dos arrays
       fossem descartados e os arrays mantivessem 5 elementos no
       total.
 - [linha 51] A derivada depende de t e x (ou x e y aqui)
       Cuidado com o nome das variáveis. A maneira como o 'x' foi
       utilizado dentro da função derivada 'funcao_aprox' poderia
       gerar confusão visto que, nesse caso, o x seria o y. O mesmo
       vale para a 'funcao_exata'.
       
'''
#Dupla: Allan Corrêa e Flávia Cruz
import numpy as np
import matplotlib.pyplot as plt

def Euler(funcao_aproximada, par_x_zero, intervalo, n_pontos):
	'''Função que calcula a aproximação de uma função através do método de Euler.
	-funcao_aproximada -> função derivada da função algo
	-par_x_zero -> um ponto da curva
	-intervalo -> intervalo do eixo x que vamos calcular a aproximação
	-n_pontos -> número de pontos para dividirmos o eixo x. Um maior número
	de pontos significa maior precisão.

	RETURN
	A função retorna uma tupla com a array de pontos x, e os valores
	aproximados do método de euler correspondentes.
	'''
	x_anterior, y_anterior = par_x_zero # desempacotamento de tupla
	h = (intervalo[1] - intervalo[0])/n_pontos
	lista_x, lista_y = [], [] # Listas com pontos x e y equivalentes

	valor_x = intervalo[0]

	for i in range(n_pontos): # Cálculo das aproximações

		valor_x += h

		y_1 = y_anterior + h*funcao_aprox(y_anterior)
		
		lista_x.append(valor_x)
		lista_y.append(y_1)

		y_anterior = y_1

	return np.array(lista_x), np.array(lista_y) # return da tupla com as arrays


funcao_aprox = lambda x: x**2 + 1 # Funçao derivada da função que queremos aproximar

funcao_exata  = lambda x: np.tan(x)
x_anterior, y_anterior = (0, 0)
intervalo = (0, 1)
n_pontos = 5

eixo_x, eixo_y_calculado = Euler(funcao_aprox, (x_anterior, y_anterior),
								 intervalo, n_pontos
								 )
eixo_y_real = np.array(funcao_exata(eixo_x))

print('''Conforme o número de pontos aumenta, a precisão também aumenta
	(vimos esse efeito plotando com 5, 20, e 200 pontos).''')

plt.title(f'Comparação das curvas com {n_pontos} pontos')
plt.plot(eixo_x, eixo_y_real, label='tan(t)')
plt.plot(eixo_x, eixo_y_calculado, label='x(t)')
plt.xticks(np.arange(0.2,1+0.2, 0.2))
plt.xlabel('valor de t')
plt.ylabel('valor de x')
plt.legend()
plt.show()
