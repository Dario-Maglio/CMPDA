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



def odesys(y, t, k1, k2, k3):
    """Define the system of equations."""
    y1, y2 = y
    dydt = [k1*y1 - k2*y1*y2,
            k2*y1*y2 - k3*y2]
    return dydt

# Parameters
k1, k2, k3 = [1., 1., 1.]
# Initial conditions
y0 = [3, 2]
# Filling the x axis
x = np.linspace(0, 10, 101)

sol = odeint(odesys, y0, x, args=(k1, k2, k3))

plt.plot(x, sol[:, 0], 'b', label='x1')
plt.plot(x, sol[:, 1], 'g', label='x2')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
