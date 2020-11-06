valor = int(input('Insira seu número inteiro')) 
divisor = valor # Definindo o valor inicial do divisor igual ao número inteiro
contagem_divisores = 0 # Variável que conta o número de divisores

while divisor > 0: 
	resto = valor % divisor
	if resto == 0: #Caso o resto seja zero, o divisor atual é um divisor
		print(divisor)
		contagem_divisores += 1 #incrementando a contagem de divisores
	divisor -= 1

print(f'Número de divisores: {contagem_divisores}')