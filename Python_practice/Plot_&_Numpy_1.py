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

plt.figure("First plot")
plt.title("Funzione")
plt.xlabel("X")
plt.ylabel("Y")
plt.errorbar(x, y, fmt='o', color = 'yellow')
plt.plot(x, model(x, *popt), marker = "o", color = 'red')
#unpacking the fit parameters with *popt
plt.show()

#--------------------------------------------------------------

# Initialization from a list
a1 = np.array([1., 2., 3])
print(a1)
# Zeros, ones, and fixed values
a2 = np.zeros(10)
a3 = np.ones((2, 2))
a4 = np.full(7, 3.)
print(a2)
print(a3)
print(a4)
# Grids, masks and functions
a5 = np.linspace(0., 10., 11)
a6 = np.log10(a5 + 10)
mask = a5 <=5.
print(a5)
print(a6)
print(mask)
print(a6[mask])

#----------------------------------------------------

import random as rd
import time as tm

start = tm.time()
x = [i*rd.random() for i in range(1, 11)] #Very SLOWER
end = tm.time() - start
print(end)
print(x)
start = tm.time()
y = np.random.random(size=10) #random in range [0,1) FASTER
end = tm.time() - start
print(end)
print(y)

#--------------------------------------------------------

from math import pi
from scipy.interpolate import InterpolatedUnivariateSpline as Spline

x = np.linspace(0., pi, 10)
y = np.sin(x) * np.exp(x)

spline1 = Spline(x, y, k=1) #Now these are two functions
spline3 = Spline(x, y, k=3)

print(spline1(pi/2))
print(spline3(pi/2))
print(spline1.integral(0., pi/2))
print(spline3.integral(0., pi/2))

xnew = np.linspace(0., pi, 20)
plt.figure("Second plot")
plt.title("Spline and functions")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(xnew, spline1(xnew), marker = "o", color = 'red', linestyle='dotted', label='First spline')
plt.plot(xnew, spline3(xnew), 'b+-', label='Second spline')
plt.plot(xnew, np.sin(xnew) * np.exp(xnew), color='yellow', marker='*',
    linestyle='dashed', linewidth=2, markersize=4, label='Real function')
plt.legend()
plt.show()
#https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html
