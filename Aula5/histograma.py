import matplotlib.pyplot as plt 
import numpy as np

valores = np.loadtxt('gravidade.dat')
print(f'Média: {np.mean(valores)}\nDesvio padrão: {np.std(valores)}')

fig, (ax1, ax2) = plt.subplots(1,2)
fig.set_size_inches((8, 4))
ax1.hist(valores, bins=20)
ax2.hist(valores, bins=60)
ax1.set_title('Valores de g, 20 bins')
ax2.set_title('Valores de g, 60 bins')
plt.savefig('histograma.png')
plt.show()
