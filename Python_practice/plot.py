import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-(2*np.pi), 2*np.pi, 50)
y = np.sin(x)

plt.plot(x, y, marker = "o", color = 'red')
plt.title("la funzione seno")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
