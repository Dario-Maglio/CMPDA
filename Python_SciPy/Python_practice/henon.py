import os
from itertools import product

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Phase space and numerical parameters
AX = -1.0
BX = 1.0
AY = AX
BY = BX
SPACEX = 0.15
SPACEY = SPACEX

# Animation and numerical parameters
STEP = 1000
FRAMES = 13

# Physical parameters
FIX_P = -0.3199
ALPHA = 0.245

# Generating colors and points
fixed_points = [(FIX_P, FIX_P)]
l1 = np.arange(AX, BX, SPACEX)
l2 = np.arange(AY, BY, SPACEY)
points = list(product(l1, l2))

#-------------------------------------------------------------------------------

def henon(valx, valy, alpha):
    return [valx*np.cos(alpha) - (valy-valx**2)*np.sin(alpha),
            valx*np.sin(alpha) + (valy-valx**2)*np.cos(alpha)]

def custom_map(x0, y0, k):
    x = np.full(STEP, x0)
    y = np.full(STEP, y0)
    index = 0
    for index in range(STEP - 1):
        x[index + 1], y[index + 1] = henon(x[index], y[index], k)
    xt = x[x<1] # Evito di plottare dati molto lontani
    yt = y[x<1]
    return xt, yt

def animate(i, ax):
    val = round(ALPHA + 0.15*ALPHA*(0.5 - i/FRAMES), 4)
    alpha = np.arccos(val)
    title = f'parametro = {val}'
    print(title)
    ax.clear()
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(AX, BX)
    ax.set_ylim(AY, BY)

    colors = iter(cm.winter(np.linspace(0, 1, len(points))))
    for valx, valy in points:
        x, y = custom_map(valx, valy, alpha)
        scat = ax.scatter(x, y, s=0.1, alpha=0.5, color=next(colors))

    for valx, valy in fixed_points:
        x, y = custom_map(valx, valy, alpha)
        scat_fix = ax.scatter(x, y, s=0.3, color='red')
        scat_fix.set_label(f'Reference Torus')

    ax.legend(loc='upper left')

def generate_gif():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10,10))
    fig.suptitle('Mappa')

    anim = animation.FuncAnimation(fig, animate, frames=FRAMES, fargs=(ax,))

    writergif = animation.PillowWriter(fps=1)
    anim.save('henon.gif', writer=writergif)
    os.system("xdg-open henon.gif")

def generate_phase_space(index):
    fig = plt.figure("Mappa", figsize=(10,10))
    ax = plt.axes(xlim=(AX, BX), ylim=(AY, BY))
    plt.title('Mappa')
    plt.xlabel('x')
    plt.ylabel('y')

    animate(index, ax)

    plt.show()

if __name__ == "__main__":

    #generate_phase_space(int(FRAMES/2))

    generate_gif()
