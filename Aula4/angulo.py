from math import pi, acos #A função acos retorna o valor do angulo em rad, baseado no cosseno
import numpy as np
from sys import exit 

def angulo(x,y):
	'''Recebe dois vetores(x e y) no formato [i, j, k]
	e retorna o valor do angulo em radianos'''	
	modulo_x = (sum(x**2))**(1/2)
	modulo_y = (sum(y**2))**(1/2)

	if modulo_x == 0 or modulo_y == 0:
		exit("Um dos vetores é zero")
	else:
		cos_teta = (sum(x*y))/(modulo_x*modulo_y)#produto escalar dos vetores dividido pelo produto dos módulos	
		cos_teta = round(cos_teta, 2)
	return acos(cos_teta) # retorna o valor do angulo teta(angulo entre os vetores x e y)

input_x = [float(x) for x in input('Insira o primeiro vetor sem espaços(ex: 2,3,4): ').split(',')]
input_y = [float(y) for y in input('Insira o segundo vetor sem espaços(ex: 2,3,4): ').split(',')]

x = np.array(input_x) # criando a primeira array, representando as coordenadas [i, j, k] do 1º vetor.
y = np.array(input_y) # criando a segunda array, representando as coordenadas [i, j, k] do 2º vetor.
angulo_radianos = angulo(x,y)
print(f'O ângulo entre os vetores, em radianos, é {round(angulo_radianos/pi, 2)}', 'π', sep='')