import numpy as np
import math as m
from prettytable import PrettyTable
import matplotlib.pyplot as mpl

# -------------------------------|ATENÇÃO|-------------------------------#
# Estou usando uma biblioteca chamada: "Prettytable", para deixar a     #
# tabela com uma aparência bonita.                                      #
#                                                                       #
# Para instalar no windows é só digitar no prompt de comando (admin):   #
# "pip3 install PTable".                                                #
# Para instalar no linux é só digitar no terminal:                      #
# "sudo pip3 install PTable".                                           #
#                                                                       #
# -----------------------------------------------------------------------#
# Para visualizar os resustados de alguma função ou método, apenas      #
# descomente a função desejada.                                         #
#                                                                       #
# E caso queira ver o grafico dessa função, descomente a função grafico #
# correspondente, e também a plot_graf no final.                        #
#                                                                       #
# -----------------------------------------------------------------------#

tabela1 = PrettyTable()
tabela1.title = "Newton"
tabela1.field_names = ["i", "x", "f(x)"]

tabela2 = PrettyTable()
tabela2.title = "Bisseccao"
tabela2.field_names = ["i", "x", "f(x)"]

tabela3 = PrettyTable()
tabela3.title = "Ponto fixo"
tabela3.field_names = ["i", "x", "f(x)"]


def f1(x):
    return m.cos(x) + 1


def d_f1(x):
    return -(m.sin(x))


def f2(x):
    return 10 + (x - 2) ** 2 - (10 * m.cos(2 * m.pi * x))


def d_f2(x):
    return 2 * x - 4 + (20 * m.pi * m.sin(2 * m.pi * x))


def f3(x):
    return x ** 3 - 3 * x ** 2 * 2 ** -x + 3 * x * 4 ** -x - 8 ** -x


def d_f3(x):
    return (
        3 * x ** 2
        - 6 * x * 2 ** -x
        - m.log(2) * 2 ** -x * -3 * x ** 2
        + 3 * 4 ** -x
        - m.log(4) * 4 ** -x * 3 * x
        + m.log(8) * 8 ** -x
    )


def f4(x):
    return m.sin(x) * m.sin((x ** 2) / m.pi)


def d_f4(x):
    return m.cos(x) * m.sin(x ** 2 / m.pi) + 2 * x / m.pi * m.cos(x ** 2 / m.pi) * m.sin(x)


def f5(x):
    return (x - 1.44) ** 5


def d_f5(x):
    return 5 * (x - 1.44) ** 4


def grafico(x, y, i):
    mpl.figure()
    mpl.subplot(211)
    mpl.plot(i, x, label="x -> f(x) = 0", color="r")
    mpl.ylabel("f(x)/x")
    mpl.legend()
    mpl.grid(True)
    mpl.subplot(212)
    mpl.plot(i, y, label="f(x) -> 0", color="b")
    mpl.xlabel("i")
    mpl.ylabel("f(x)/x")
    mpl.legend()
    mpl.grid(True)


def graficof(x, y):
    mpl.figure()
    mpl.plot(x, y, color="g")
    mpl.xlabel("x")
    mpl.ylabel("f(x)")
    mpl.grid(True)


def plot_graf():
    mpl.show()


def funcao(fx, xv, fxv, a, b):

    for i in range(a * 10, b * 10 + 1):
        j = i / 10
        xv.append(j)
        fxv.append(fx(j))

    # print(xv, fxv, sep = '\n')
    # print("")


def bissecao(a, b, fx, xv, fxv, iv):

    for i in range(1000):

        m = (a + b) / 2
        xv.append(m)
        fxv.append(fx(m))
        iv.append(i)
        tabela2.add_row([iv[i], xv[i], fxv[i]])

        if abs(fx(m)) < erro:
            print(tabela2, end="\n")
            tabela2.clear_rows()
            break

        else:
            if ((fx(m)) * (fx(b))) < 0:
                a = m
            else:
                b = m


def newton(fx, dfx, x, xv, fxv, iv):

    xv.append(x)
    fxv.append(f1(x))
    iv.append(0)
    tabela1.add_row([iv[0], xv[0], fxv[0]])

    for i in range(1, 1000):

        xv.append(xv[i - 1] - (fx(xv[i - 1]) / dfx(xv[i - 1])))
        fxv.append(fx(xv[i]))
        iv.append(i)

        tabela1.add_row([iv[i], xv[i], fxv[i]])

        if abs(fxv[i]) < erro:
            print(tabela1, end="\n")
            tabela1.clear_rows()
            break


def ponto_fixo1(x):

    xp1.append(x)
    fxp1.append(f1(x))
    ip1.append(0)

    tabela3.add_row([ip1[0], xp1[0], fxp1[0]])

    for i in range(1, 1000):

        xp1.append(xp1[i - 1] + f1(xp1[i - 1]) * 14)
        fxp1.append(f1(xp1[i]))
        ip1.append(i)

        tabela3.add_row([ip1[i], xp1[i], fxp1[i]])

        if abs(fxp1[i]) < erro:
            print(tabela3, end="\n")
            tabela3.clear_rows()
            break


def ponto_fixo2(x):

    xp2.append(x)
    fxp2.append(f2(x))
    ip2.append(0)

    tabela3.add_row([ip2[0], xp2[0], fxp2[0]])

    for i in range(1, 2000):

        xp2.append(xp2[i - 1] - f2(xp2[i - 1]) / 20)
        fxp2.append(f2(xp2[i]))
        ip2.append(i)

        tabela3.add_row([ip2[i], xp2[i], fxp2[i]])

        if abs(fxp2[i]) < erro:
            print(tabela3, end="\n")
            tabela3.clear_rows()
            break


def ponto_fixo3(x):

    xp3.append(x)
    fxp3.append(f3(x))
    ip3.append(0)

    tabela3.add_row([ip3[0], xp3[0], fxp3[0]])

    for i in range(1, 1000):

        xp3.append(xp3[i - 1] - f3(xp3[i - 1]) * 5)
        fxp3.append(f3(xp3[i]))
        ip3.append(i)

        tabela3.add_row([ip3[i], xp3[i], fxp3[i]])

        if abs(fxp3[i]) < erro:
            print(tabela3, end="\n")
            tabela3.clear_rows()
            break


def ponto_fixo4(x):

    xp4.append(x)
    fxp4.append(f4(x))
    ip4.append(0)

    tabela3.add_row([ip4[0], xp4[0], fxp4[0]])

    for i in range(1, 1000):

        xp4.append(xp4[i - 1] - f4(xp4[i - 1]) * 4 / (xp4[i - 1]))
        fxp4.append(f4(xp4[i]))
        ip4.append(i)

        tabela3.add_row([ip4[i], xp4[i], fxp4[i]])

        if abs(fxp4[i]) < erro:
            print(tabela3, end="\n")
            tabela3.clear_rows()
            break


def ponto_fixo5(x):

    xp5.append(x)
    fxp5.append(f5(x))
    ip5.append(0)

    tabela3.add_row([ip5[0], xp5[0], fxp5[0]])

    for i in range(1, 1000):

        xp5.append(xp5[i - 1] - f5(xp5[i - 1]) * 50 / xp5[i - 1] ** 2)
        fxp5.append(f5(xp5[i]))
        ip5.append(i)

        tabela3.add_row([ip5[i], xp5[i], fxp5[i]])

        if abs(fxp5[i]) < erro:
            print(tabela3, end="\n")
            tabela3.clear_rows()
            break


xp1 = []
fxp1 = []
ip1 = []
xp2 = []
fxp2 = []
ip2 = []
xp3 = []
fxp3 = []
ip3 = []
xp4 = []
fxp4 = []
ip4 = []
xp5 = []
fxp5 = []
ip5 = []
xn1 = []
fxn1 = []
in1 = []
xn2 = []
fxn2 = []
in2 = []
xn3 = []
fxn3 = []
in3 = []
xn4 = []
fxn4 = []
in4 = []
xn5 = []
fxn5 = []
in5 = []
x1 = []
fx1 = []
x2 = []
fx2 = []
x3 = []
fx3 = []
x4 = []
fx4 = []
x5 = []
fx5 = []
xb3 = []
fxb3 = []
ib3 = []
xb4 = []
fxb4 = []
ib4 = []
xb5 = []
fxb5 = []
ib5 = []
erro = 1e-6

# ----------------|Newton|----------------#
# newton(f1, d_f1, 1, xn1, fxn1, in1)
# newton(f2, d_f2, 1.6, xn2, fxn2, in2)
# newton(f3, d_f3, 4, xn3, fxn3, in3)
# newton(f4, d_f4, 1, xn4, fxn4, in4)
# newton(f5, d_f5, 1.6, xn5, fxn5, in5)

# grafico(xn1, fxn1, in1)
# grafico(xn2, fxn2, in2)
# grafico(xn3, fxn3, in3)
# grafico(xn4, fxn4, in4)
# grafico(xn5, fxn5, in5)
# ----------------------------------------#

# --------------|Ponto fixo|--------------#
# ponto_fixo1(3)
# ponto_fixo2(2.1)
# ponto_fixo3(1)
# ponto_fixo4(2)
# ponto_fixo5(2)

# grafico(xp1, fxp1, ip1)
# grafico(xp2, fxp2, ip2)
# grafico(xp3, fxp3, ip3)
# grafico(xp4, fxp4, ip4)
# grafico(xp5, fxp5, ip5)
# ----------------------------------------#

# --------------|Bissecçõo|---------------#
# bissecao(0, 3, f3, xb3, fxb3, ib3)
# bissecao(-1, 2, f4, xb4, fxb4, ib4)
# bissecao(0, 10, f5, xb5, fxb5, ib3)

# grafico(xb3, fxb3, ib3)
# grafico(xb4, fxb4, ib4)
# grafico(xb5, fxb5, ib3)
# ----------------------------------------#

# ---------------|Funções|----------------#
# funcao(f1, x1, fx1, -10, 10)
# funcao(f2, x2, fx2, -12, 16)
# funcao(f3, x3, fx3, -3, 10)
# funcao(f4, x4, fx4, -10, 10)
# funcao(f5, x5, fx5, -7, 10)

# graficof(x1, fx1)
# graficof(x2, fx2)
# graficof(x3, fx3)
# graficof(x4, fx4)
# graficof(x5, fx5)
# ----------------------------------------#

# plot_graf()
