import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt



# Global parameters
N = 11
AX = 0.0
BX = 1.0
AX2 = AX + 0.5
BX2 = BX - 0.0001
SPACEX = 0.0005
STEPS = 40
X0 = 0.1
X02 = 0.7

#-------------------------------------------------------------------------------

def logistic(x0, par):
    return 4. * par * (1. - x0) * x0

def dlogic(x0, par):
    return 4. * par * (1. - 2 * x0)

def plot_lambda():
    fig, axs = plt.subplots(3, 3, num="Logistic map", figsize=(20,20))
    fig.suptitle("Logistic map")

    mask = np.ones(N, dtype=bool)
    mask[[0, N-1]] = False
    lamb = np.linspace(AX, BX, N)[mask]
    xgrid = np.linspace(AX, BX, N)

    for ax, val in zip(axs.flat, lamb):
        title = f'$\lambda$ = {round(val, 2)}'
        print(title)

        ax.set_title(title)
        ax.set(xlabel='$x_n$', ylabel='$x_{n+1}$', xlim=(AX, BX), ylim=(AX, BX))
        ax.label_outer()

        ax.plot(xgrid, xgrid, color='g', label="Fixed points")
        ax.plot(xgrid, logistic(xgrid, val), color='r', label="Logi map")

        x = np.full(STEPS, X0)
        y = np.full(STEPS, X0)
        for iter in range(STEPS - 1):
            y[iter] = logistic(x[iter], val)
            x[iter + 1] = y[iter]
        y[STEPS-1] = logistic(x[STEPS-1], val)

        ax.scatter(x, y, color='black', label="Evolution")

        ax.legend(loc='upper left')

    plt.savefig("map_logistic_lambda.png")
    plt.show()

def plot_chaos():
    plt.figure("Chaos in logistic map", figsize=(15,15))
    plt.title("Logistic map and Lyapunov exponent")
    plt.xlim(AX2, BX)
    plt.ylim(-AX2, BX)

    lamb = np.arange(AX2, BX2, SPACEX)
    sigma = np.zeros_like(lamb)

    plt.plot(lamb, sigma, "r--", lw=0.5)

    for index, val in enumerate(lamb):
        x = X02
        for iter in range(100 * STEPS):
            x = logistic(x, val)

        l = np.full(STEPS + 1, val)
        x = np.full(STEPS + 1, x)
        f = np.zeros(STEPS)
        for iter in range(STEPS):
            x[iter + 1] = logistic(x[iter], val)
            f[iter] = abs(dlogic(x[iter], val))

        sigma[index] = np.sum(np.log(f)) / STEPS

        print(f"lambda: {round(val, 3)} sigma: {round(sigma[index], 3)}")

        plt.scatter(l, x, s=0.1, color="black")

    plt.plot(lamb, sigma, color="b", lw=0.5)
    plt.savefig("map_logistic_Lyapunov.png")
    plt.show()

#-------------------------------------------------------------------------------

if __name__ == "__main__":

    plot_lambda()

    plot_chaos()
