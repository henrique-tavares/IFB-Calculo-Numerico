from __future__ import division
import matplotlib.pyplot as mpl
import math as m

sen_x = []
sen_y = []
sen_x_taylor = []
sen_y_taylor = []

for i in range(0, 361, 10):
    senX = 0
    x = m.radians(i)

    for j in range(0, 30):
        sinal = (-1) ** j
        senX += sinal * ((x ** ((2 * j) + 1)) / (m.factorial(((2 * j) + 1))))

    sen_y_taylor.append(senX)
    sen_x_taylor.append(i)

for i in range(0, 361):
    sen_y.append(m.sin(m.radians(i)))
    sen_x.append(i)

mpl.plot(sen_x, sen_y, label="sen(x)")
mpl.plot(sen_x_taylor, sen_y_taylor, color="#32CD32", label="sen(x)_taylor", linestyle="dotted")
mpl.ylabel("sen(x)")
mpl.xlabel("x")
mpl.legend()
mpl.grid(True)
mpl.show()
