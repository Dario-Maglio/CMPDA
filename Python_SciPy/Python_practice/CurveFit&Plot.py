print('\nFit  example!\n\n')

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0., 10., 10) #9 punti
y = x**3 + 3*x
yer = x*10

def model(x, a, b):
    return a*x**3 + b*x

for item1, item2 in zip(x, y):
    print(item1, item2)

popt, pcov = curve_fit(model, x, y)

plt.figure("Figura 1") #Create a canvas (tela)
plt.errorbar(x, y, fmt='o', yerr=yer, label='Points')
plt.plot(x, model(x, *popt), label='Function')
plt.xlabel('Numeri')
plt.ylabel('Risultati')
plt.legend(loc='lower right')

plt.figure("Figura 2")
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, x**2, yerr=yer, uplims=upperlimits, lolims=lowerlimits,
            label='Subsets of uplims and lolims')
plt.plot(x, model(x, popt[0], popt[1]), 'k', label='Function x**2')
plt.legend(loc='upper left')

plt.show()

#---------------------------------------------
print('\n\nSpline  example!\n\n')

from math import pi
from scipy.interpolate import InterpolatedUnivariateSpline as Spline

x = np.linspace(0., pi, 10)
y = np.sin(x) * np.exp(x)

#Spline is the interpolated function
#We can add w=y error vector
#K Degree of the smoothing spline. Must be 1 <= k <= 5
spline1 = Spline(x, y, k=1)
spline2 = Spline(x, y, k=3)

print(spline1(pi/2))
print(spline2(pi/2))
print(spline1.get_residual())
print(spline2.get_residual())
print(spline1.derivative(n=1)(pi/2))
print(spline2.derivative(n=1)(pi/2))
print(spline1.integral(0., pi/2))
print(spline2.integral(0., pi/2))
print(spline2.roots())

xnew = np.linspace(1.5, pi, 10)
plt.figure("New plot")
plt.title("Spline and fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(xnew, np.sin(xnew) * np.exp(xnew), color='b', marker='*', linewidth=2, markersize=4, label='Real function')
plt.plot(xnew, spline1(xnew), marker = "o", color = 'red', linestyle='dotted', label='First spline')
plt.plot(xnew, spline2(xnew), 'g+--', label='Second spline')
plt.legend()
plt.show()

spline3 = Spline(x, y, k=5)
dspline3= spline3.derivative(n=1)
def ispline3(x):
    return [spline3.integral(0., i) for i in x]

xnew = np.linspace(0., pi, 20)
plt.figure("Spline functions")
plt.title("Spline and functions")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(xnew, spline3(xnew), color='b', marker='*', linewidth=2, markersize=4, label='Real function')
plt.plot(xnew, dspline3(xnew), marker = "o", color = 'red', linestyle='dotted', label='derivate spline')
plt.plot(xnew, ispline3(xnew), 'g+--', label='integral spline')
plt.legend()
plt.show()

#https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html
