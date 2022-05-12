""" Script for bidimensional and complex functions visualization """

import pylab
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# Choose the configuration
SURFACE = False
COMPLEX = not(SURFACE)

# Global parameters
AX = -1
BX = 1
SPACEX = 0.005
AY = AX
BY = BX
SPACEY = SPACEX
AZ = -10.
BZ = 10.

# Grid
X = np.arange(AX, BX, SPACEX)
Y = np.arange(AY, BY, SPACEY)

#-------------------------------------------------------------------------------

def fun(x, y):
    """Function to evaluate"""
    z = 100 * (x**2 + y**2)
    return np.exp(-z) + 0.3*np.sin(z/(np.sqrt(z) + 1.))

def cfun(z):
    """Complex function to evaluate"""
    g = 0.1
    ohm = 0.5
    z = (z + 0.5*g)**2 + ohm**2 - (0.5*g)**2
    return 1./ z

#-------------------------------------------------------------------------------

fig = plt.figure("Function", figsize=(15,10))

x, y = np.meshgrid(X, Y)

if SURFACE:
    fig.suptitle("Surface visualization")
    ax = fig.add_subplot(projection='3d')

    # Evaluate the function
    z = fun(x.ravel(), y.ravel()).reshape(x.shape)

    # Clipping singularities
    # mask = (z<AZ) + (z>BZ)
    # z[mask]= np.nan

    # Visualization
    surf = ax.plot_surface(x, y, z, cmap=cm.viridis)
    fig.colorbar(surf, shrink=0.5, aspect=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('fun(x,y)')
    #ax.set_zlim(-AZ, BZ)

    fig.savefig('surface_visualization.png')

else:
    fig.suptitle("Complex function visualization")
    axis = [fig.add_subplot(1, 2, k+1, projection='3d') for k in range(2)]

    # Evaluate the function
    z = cfun(x + 1j * y)

    # Clipping singularities
    mask = (z.real<AZ) + (z.real>BZ)
    z.real[mask]= np.nan
    mask = (z.imag<AZ) + (z.imag>BZ)
    z.imag[mask]= np.nan

    # Visualization
    axis[0].set_title("Real part")
    real = axis[0].plot_surface(x, y, z.real, cmap=cm.viridis)
    fig.colorbar(real, ax=axis[0], shrink=0.5, aspect=10)
    axis[1].set_title("Imaginary part")
    imag = axis[1].plot_surface(x, y, z.imag, cmap=cm.viridis)
    fig.colorbar(imag, ax=axis[1], shrink=0.5, aspect=10)
    for ax in axis:
        ax.set_xlabel('Re z')
        ax.set_ylabel('Im z')
        ax.set_zlim(AZ, BZ)

    fig.savefig('surface_visualization_c.png')

plt.show()

#-------------------------------------------------------------------------------

if COMPLEX:
    fig = plt.figure("Function projections", figsize=(10,8))
    fig.suptitle("Complex function projections")
    axis = [fig.add_subplot(2, 2, k+1) for k in range(4)]

    # Evaluate the function
    x = X #+ 1j * np.full_like(X, 0.00001)
    y = 1j * Y

    FunOnRe = cfun(x)
    FunOnIm = cfun(-y)

    x = np.real(x)
    y = np.imag(y)

    # Plot
    axis[0].set_title("Real part evaluated on real numbers")
    axis[0].plot(x, FunOnRe.real)
    axis[1].set_title("Imag part evaluated on real numbers")
    axis[1].plot(x, FunOnRe.imag)
    axis[2].set_title("Real part evaluated on imag numbers")
    axis[2].plot(y, FunOnIm.real)
    axis[3].set_title("Imag part evaluated on imag numbers")
    axis[3].plot(y, FunOnIm.imag)

    fig.savefig('surface_projections_c.png')
    plt.show()
