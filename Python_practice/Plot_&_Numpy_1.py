import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0., 10., 30)
y = np.sin(x)

def model(x, a, m, q):
    return m * x + q + a * (x**2)

popt, pcov = curve_fit(model, x, y)
print(popt) #optimal parameters
print(pcov) #covariance matrix

plt.title("Funzione")
plt.xlabel("X")
plt.ylabel("Y")
plt.errorbar(x, y, fmt='o', color = 'yellow')
plt.plot(x, model(x, *popt), marker = "o", color = 'red')
#unpacking the fit parameters with *popt
plt.show()
