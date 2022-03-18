import os
from itertools import product

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# Phase space and numerical parameters
AX = 0.0
#AX = -1.0
BX = 1.0
AY = AX
BY = BX
SPACEX = 0.15
SPACEY = SPACEX

# Animation and numerical parameters
STEPS = 1000
FRAMES = 23

# Physical parameters
# FIX_P = -0.3199
# ALPHA = 0.245
# FACTOR = 0.15 * ALPHA
FIX_P = 0.61
ALPHA = 0.975
FACTOR = 0.2 * ALPHA

# Generating colors and points
fixed_points = [(FIX_P, FIX_P)]
l1 = np.arange(AX, BX, SPACEX)
l2 = np.arange(AY, BY, SPACEY)
points = list(product(l1, l2))

#-------------------------------------------------------------------------------

def henon(valx, valy, alpha):
    alpha = np.arccos(alpha)
    return [valx*np.cos(alpha) - (valy-valx**2)*np.sin(alpha),
            valx*np.sin(alpha) + (valy-valx**2)*np.cos(alpha)]

def stdmap(valx, valy, alpha):
    p = valy + alpha*np.sin(2*np.pi*valx)/(2*np.pi)
    return [np.mod(valx + p, 1), np.mod(p, 1)]

cmap = stdmap

#-------------------------------------------------------------------------------

def custom_map(x0, y0, k):
    x = np.full(STEPS, x0)
    y = np.full(STEPS, y0)
    for index in range(STEPS - 1):
        x[index + 1], y[index + 1] = cmap(x[index], y[index], k)
    mask = (x>AX)&(x<BX)&(y>AY)&(y<BY)
    xt = x[mask] # Evito di plottare dati molto lontani
    yt = y[mask]
    return xt, yt

def animate(i, ax):
    val = round(ALPHA + FACTOR*(i/FRAMES - 0.5), 4)
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
        x, y = custom_map(valx, valy, val)
        scat = ax.scatter(x, y, s=0.1, alpha=0.5, color=next(colors))

    for valx, valy in fixed_points:
        x, y = custom_map(valx, valy, val)
        scat_fix = ax.scatter(x, y, s=0.3, color='red')
        scat_fix.set_label(f'Reference Torus')

    ax.legend(loc='upper left')

def generate_gif():
    #plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10,10))
    fig.suptitle('Mappa')

    anim = animation.FuncAnimation(fig, animate, frames=FRAMES, fargs=(ax,))

    writergif = animation.PillowWriter(fps=1)
    anim.save('map_std.gif', writer=writergif)
    os.system("xdg-open map_std.gif")

def generate_phase_space(index):
    fig = plt.figure("Mappa", figsize=(10,10))
    ax = plt.axes(xlim=(AX, BX), ylim=(AY, BY))
    plt.title('Mappa')
    plt.xlabel('x')
    plt.ylabel('y')

    animate(index, ax)

    plt.show()

def phase_plot():
    g,L = 1., 0.5
    xvalues, yvalues = np.meshgrid(4*l1, 4*l2)
    print('Meshgrid creata')
    xdot = yvalues
    ydot = -g/L*np.sin(xvalues)
    print('Creo il plot...')
    plt.figure("Phase space")
    plt.streamplot(xvalues, yvalues, xdot, ydot, color='black', linewidth=0.5)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$p$')
    plt.savefig("map_phase_space.png")
    plt.show()

if __name__ == "__main__":

    #phase_plot()

    #generate_phase_space(int(FRAMES/2))

    generate_gif()
