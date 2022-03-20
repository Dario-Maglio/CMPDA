import os

import numpy as np
import matplotlib.pyplot as plt

from fractal_dimension import fractal_dimension_3D



N = 500000
S, R, B  = 10., 28., 8/3
STEP = 0.001
X0, Y0, Z0 = 0.1, 0., 0.

#-------------------------------------------------------------------------------

def lorentz(x, y, z, h, s, r, b):
    for i in range(len(x) - 1):
        x1 =  h * (s * ( y[i] - x[i] ))
        y1 =  h * (-x[i] * z[i] + r * x[i] - y[i])
        z1 =  h * (x[i] * y[i] - b * z[i])

        x2 = h * (s * ( y1 - x1 ))
        y2 = h * (-x1 * z1 + r * x1 - y1)
        z2 = h * (x1 * y1 - b * z1)

        x[i+1] = x[i] + 0.5 * (x1 + x2)
        y[i+1] = y[i] + 0.5 * (y1 + y2)
        z[i+1] = z[i] + 0.5 * (z1 + z2)

def fractal_calculation(x, y, z):
    lx = 10 * int(np.amax(x) - np.amin(x) + 1)
    ly = 10 * int(np.amax(y) - np.amin(y) + 1)
    lz = 10 * int(np.amax(z) - np.amin(z) + 1)

    points = np.stack((x,y,z), axis=1)
    box, edges = np.histogramdd(points, bins=(lx, ly, lz))

    return fractal_dimension_3D(box, n_offsets=10, plot=True)

#-------------------------------------------------------------------------------

def display_lorentz():
    fig = plt.figure("Lorenz", figsize=(15,15))
    fig.suptitle("Lorenz attractor")
    axis = [fig.add_subplot(2, 2, k + 1, projection='3d') for k in range(4)]

    v0 = np.ones(N)
    x, y, z = v0*X0, v0*Y0, v0*Z0

    lorentz(x, y, z, STEP, S, R, B)

    for ax in axis:
        ax.scatter(x, y, z, s=0.0003)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

    axis[0].view_init(70, 0)
    axis[2].view_init(20, 0)
    axis[3].view_init(20, 90)

    plt.tight_layout()
    plt.savefig('lorenz_attractor.png')

    dimens = fractal_calculation(x, y, z)
    print(f"Fractal dimension: {dimens}")
    plt.title("Fractal dimension : 2.0627160")
    plt.savefig('lorenz_dimension.png')



if __name__ == "__main__":

    display_lorentz()
