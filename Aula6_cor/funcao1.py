'''
 - Sem erros.

OBS: Eixos sem rótulo
OBS: Figura mostra função só até x = 3.9
'''

#Allan Bruno(IFA) e Lorena Dias(IFB)
import numpy as np
import matplotlib.pyplot as plt
# Lambda que calcula a funçao pedida na questão
funcao1 = lambda array: np.exp(-array) - np.sin(np.pi*array/2)
step = 0.1
eixo_x = np.arange(0, 4 + step, step)# Array eixo x
eixo_y = funcao1(eixo_x)# Array eixo y

plt.plot(eixo_x, eixo_y)#plot do gráfico
plt.savefig('funcao1.pdf')
plt.show()

