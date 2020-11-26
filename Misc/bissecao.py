from __future__ import division
import matplotlib.pyplot as mpl
import numpy as np

a = -5.2
b = 0.1
iteracoes = 1000
erro = 1e-3


def f(x):
    return x ** 3 - 8 * x ** 2 - 2 * x + 1


i0 = []
x0 = []
graf = []

for i in range(0, iteracoes):
    if abs(b - a) < erro:
        break

    else:
        x = (b + a) / 2
        if np.sign(f(x)) * np.sign(f(a)) < 0:
            b = x
            if abs(b - a) < erro:
                break
        elif np.sign(f(x)) * np.sign(f(b)) < 0:
            a = x
            if abs(b - a) < erro:
                break

        i0.append(i)
        x0.append(x)
        graf.append(f(x))

    print(i, a, b, x, f(x))

mpl.plot(i0, graf, label="Indo pra zero")
mpl.plot(i0, x0, label="Indo pra raiz")
mpl.ylabel("f(x)/x")
mpl.xlabel("i")
mpl.legend()
mpl.grid(True)
mpl.show()