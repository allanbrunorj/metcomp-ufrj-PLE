import numpy as np  #Importando numpy
with open('media.txt') as f: # Bloco identado que lê o arquivo com as notas
	'''1 - Lendo as notas, tirando "\n" do final, transformando em float,
	   criando uma lista e transformando em array'''
	lista_notas = np.array([float(x.rstrip('\n')) for x in f.readlines()])


print('-'*15, 'Programa da média','-'*16)
print(f'As notas da turma são {lista_notas}') #Imprimindo np.array
print('-'*50)

len_notas = len(lista_notas)# Quantidade de notas
print(f'Alunos na turma: {len_notas}')

media_turma = round(lista_notas.sum()/len_notas, 1) #Média da turma calculada
media_np = round(lista_notas.mean(), 1) #Média calculada pelo np
print(f'A média(calculada) da turma é {media_turma}')
print(f'A média do numpy é {media_np}')
print('-'*50)

soma_desvio = 0 #Declarando variável pra calcular o desvio
for i in range(len_notas): #Esse loop calcula a parte de soma do desvio padrão^2
	soma_desvio += (lista_notas[i] - media_np)**2

desvio_padrao_calculado = round(np.sqrt(soma_desvio/(len_notas-1)), 1) #Fim do calculo, raiz quadrada e round
print(f'O desvio padrão(calculado) é {desvio_padrao_calculado}')
print(f'O desvio padrão do Numpy é {round(lista_notas.std(), 1)}')
print('-'*50)
#List comprehension para saber qtd acima ou igual a 7, e abaixo de 3
print(f'{len([x for x in lista_notas if x >= 7])}´alunos passaram direto') 
print(f'{len([x for x in lista_notas if x < 3])} alunos reprovaram direto')


