from __future__ import division
import matplotlib.pyplot as mpl
import numpy as np
import math as m


def f(x):
    return 10 + (x - 2) ** 2 - 10 * m.cos(2 * m.pi * m.radians(x))


def df(x):
    return 2 * x - 4 + 20 * m.pi * m.sin(2 * m.pi * m.radians(x))


erro = 1e-5
x = []
graf = []
i0 = []

i0.append(0)
x.append(0)
graf.append(f(x[0]))

print(i0[0], x[0], graf[0])

for i in range(1, 1000):

    x.append(x[i - 1] - (f(x[i - 1]) / df(x[i - 1])))

    i0.append(i)
    graf.append(f(x[i]))

    print(i, x[i], graf[i])

    if abs(graf[i]) < erro:
        break

mpl.subplot(211)
mpl.plot(i0, x, label="Indo pra raiz mais próxima de f(x) com g(x)\ng(x) = x - f(x)/f'(x)")
mpl.xlabel("i")
mpl.ylabel("g(x)")
mpl.grid(True)
mpl.legend()
mpl.subplot(212)
mpl.plot(i0, graf, label="f(x) indo pra 0")
mpl.xlabel("i")
mpl.ylabel("f(x)")
mpl.grid(True)
mpl.legend()
mpl.show()
