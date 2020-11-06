from math import sqrt
# Recebendo os inputs para os 3 coeficientes
a = float(input('Insira o coeficiente de x²: '))
b = float(input('Insira o coeficiente de x: '))
c = float(input('Insira o termo independente: '))

delta = b**2 - 4*a*c #calculando delta
if (-1e-5 <= delta <= 1e-5): # Condição que transforma deltas muito próximos de zero(possíveis resquícios binários) em zero.
	delta = 0

modulo_de_delta = abs(delta) #Função que retorna o valor absoluto de delta. Delta só é alterado se for < 0.
termo1 = round(-b/(2*a), 2) # O segundo parâmetro(2), é o numero de casas decimais, para melhor visualização
termo2 = round(sqrt(modulo_de_delta)/(2*a), 2)

if delta < 0:	
	print(f'A função tem raízes complexas, sendo elas: {termo1} + {termo2}j e {termo1} - {termo2}j')

if delta == 0:
	print(f'A função tem uma única raiz, que é: {termo1}')

if delta > 0:
	print(f'A função tem duas raízes reais, sendo elas: {round(termo1+termo2, 2)} e {round(termo1 - termo2, 2)}')






