# Hazme un programa que grafique los archivos RewardsEnv1.txt y RewardsEnv2.txt
# en una misma gráfica. El eje x es el número de episodios y el eje y es el reward

import matplotlib.pyplot as plt
import numpy as np

# Cargamos los datos
datos1 = np.loadtxt('RewardsEnv1.txt')
datos2 = np.loadtxt('RewardsEnv2.txt')

# Graficamos
plt.plot(datos1, label='Env1')
plt.plot(datos2, label='Env2')
plt.xlabel('Episodios')
plt.ylabel('Reward')
plt.legend()
plt.show()
