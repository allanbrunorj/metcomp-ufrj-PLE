'''
sem erros
'''


def mysum(lista):
	'''Função que recebe uma array como argumento, e retorna a soma dessa array.
	Os tipos de variável presentes na array precisam ser compatíveis numa soma
	(int e float são, float e string não).'''
	soma = lista[0]
	for value in lista[1:]:
		soma += value
	return soma


# Alterne o comentário entre as listas abaixo pra testar a funcionalidade do programa.
lista_teste = [1, 2, 3]
# lista_teste = ['Hello, ', 'World!']
# lista_teste = [[1,2], [4,3]]

print(mysum(lista_teste))
