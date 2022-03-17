"""Basic ode integration script.
The odeint method uses the lsoda integrator from FORTRAN. lsoda differs from the
other integrators (except lsodar) in that it switches automatically between
stiff and nonstiff methods. This means that the user does not have to determine
whether the problem is stiff or not, and the solver will automatically choose
the appropriate method. It always starts with the nonstiff method.

An ordinary differential equation problem is stiff if the solution being sought
is varying slowly, but there are nearby solutions that vary rapidly, so the
numerical method must take small steps to obtain satisfactory results.

Ref:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



# Parameters
A = 0.
B = 1.
STEPS = 10000

# Filling the x axis
xgrid = np.linspace(A, B, STEPS)

#-------------------------------------------------------------------------------

def odesys(y, t, k1, k2, k3):
    """Define the system of equations in the form of dydt = M * y ."""
    y1, y2 = y
    dydt = [k1*y1 - k2*y1*y2,
            k2*y1*y2 - k3*y2]
    return dydt

def fun(x):
    """Define the stochastic functions in the form dx = f(x)*dt + g(x)*dw ."""
    f = np.full_like(x, 0.)
    g = x
    return [f, g]

def dfun(x):
    """Define the derivatives of the stochastic functions."""
    df = np.full_like(x, 0.)
    dg = np.full_like(x, 0.)
    return [df, dg]


def heun(x0, dt, z, fun, dfun):
    z = np.sqrt(dt) * z

    f0, g0 = fun(x0)
    dfdt0, dgdt0 = dfun(x0)
    x1 = z*g0 + f0*dt + 0.5*g0*dgdt0*(z**2)

    f1, g1 = fun(x1)
    dfdt1, dgdt1 = dfun(x1)
    x2 = z*g1 + f1*dt + 0.5*g1*dgdt1*(z**2)

    return x0 + 0.5*(x1 + x2)

#-------------------------------------------------------------------------------

def ode_solver():
    plt.figure("ODE soultion")
    y0 = [0.5, 0.5]
    k1, k2, k3 = [10, 10, 10]
    sol = odeint(odesys, y0, xgrid, args=(k1, k2, k3))

    plt.plot(xgrid, sol[:, 0], 'b', label='prede')
    plt.plot(xgrid, sol[:, 1], 'g', label='predatori')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

def sde_solver():
    plt.figure("SDE soultion")
    y0 = 0.5
    dt = [xgrid[i+1]-xgrid[i] for i in range(STEPS - 1)]
    z = np.random.normal(size=(STEPS))
    y = np.full(STEPS, y0)
    for index in range(STEPS - 1):
        y[index + 1] = heun(y[index], dt[index], z[index], fun, dfun)

    plt.plot(xgrid, y, 'b', label='x')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

#-------------------------------------------------------------------------------

if __name__=="__main__":

    ode_solver()

    sde_solver()
