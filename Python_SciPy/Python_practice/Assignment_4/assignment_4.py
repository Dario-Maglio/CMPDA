"""Assignment 4 basic"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as Spline

class ProbabilityDensityFunction:
    """this class generates pseudo random number generator with a pdf given as
       input through a set of points
    """

    def __init__(self, x, y, o = 3):
        """makes a spline of order o, on the x interval of the
           probability density function associated to y.
           It is not normalized by default
        """
        self._x = x
        self._y = y
        self._o = o
        self._spline = Spline(self._x, self._y, k = self._o)
        normal = self._spline.integral(x[0], x[-1])
        print(f'the spline normalization coefficent is {normal}')
        self._y = self._y / normal
        self._spline = Spline(self._x, self._y, k = self._o)

    def __call__(self, points):
        """evaluates the class on a set of points, returning the associated pdf
        """
        return self._spline(points)

    def interval(self, a, b):
        """calculates the probability for the random variable to be included in
           a generic interval
        """
        return self._spline.integral(a, b)

    def random(self):
        """throws random numbers according to the given distribution
        """
        f = np.array([self.interval(self._x[0], item) for item in self._x])
        freverse = Spline(f, self._x, k = self._o)
        return freverse(np.random.random())

    def random_array(self, len):
        """creates an array with random numbers according to the distribution
        """
        return np.array([self.random() for i in range(len)])



if __name__ == '__main__':
    """Here we test the functionalities of our class."""
    a = -5.
    b = -a
    n = 101
    x = np.linspace(a, b, n)
    x0 = np.linspace(a/2, b/2, int(n/2))

    y1 = np.full(n, 1/(b-a))
    homogeneus = ProbabilityDensityFunction(x, y1)
    print(homogeneus(x0))
    print(homogeneus.interval(a, 0.))
    r1 = homogeneus.random_array(100*n)
    plt.figure('Omogenea')
    plt.title('Distribuzione')
    plt.xlabel('Dominio')
    plt.ylabel('Frequenza')
    nn, bi, patches = plt.hist(r1, density=True)
    plt.show()

    y2 = np.exp(-(x**2)/2)/np.sqrt(2 * np.pi)
    gauss = ProbabilityDensityFunction(x, y2)
    print(gauss(x0))
    print(gauss.interval(a, 0.))
    r2 = gauss.random_array(100*n)
    plt.figure('Gauss')
    plt.title('Distribuzione')
    plt.xlabel('Dominio')
    plt.ylabel('Frequenza')
    nn, bi, patches = plt.hist(r2, bins=n, density=True)
    plt.show()


    y3 = np.exp(-x)
    gauss = ProbabilityDensityFunction(x, y3)
    print(gauss(x0))
    print(gauss.interval(a, 0.))
    r3 = gauss.random_array(100*n)
    plt.figure('Strange')
    plt.title('Distribuzione')
    plt.xlabel('Dominio')
    plt.ylabel('Frequenza')
    nn, bi, patches = plt.hist(r3, bins=n, density=True)
    plt.show()
