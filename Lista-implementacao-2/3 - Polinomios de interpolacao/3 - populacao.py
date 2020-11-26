import numpy as np
import math as m
import matplotlib.pyplot as mpl

anos = [
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
]
populacao = [
    6115108363,
    6194460444,
    6273526441,
    6352677699,
    6432374971,
    6512602867,
    6593623202,
    6675130418,
    6757887172,
    6840591577,
    6922947261,
    7004011262,
    7086993625,
    7170961674,
    7255653881,
    7340548192,
    7426103221,
    7510990456,
    7594270356,
]

N1 = np.zeros((18, 17))
N2 = np.zeros((4, 3))
N3 = np.zeros((20, 19))

xn1 = []
xn2 = []
xl1 = []
xl2 = []
pxn1 = []
pxn2 = []
pxl1 = []
pxl2 = []


def p_de_x(p, n, n2, n3, x, y, a, b, offset, n4):

    for i in range(a * 10, b * 10 + 1):
        i /= 10
        x.append(i)
        y.append(p(n, n2, n3, i, offset, n4))


def grafico3(x1, y1, label1, x2, y2, label2, x3, y3, label3, title):
    mpl.figure()
    mpl.title(title)
    mpl.plot(x1, y1, label=label1, color="r", alpha=0.7)
    mpl.plot(x2, y2, label=label2, color="b", alpha=0.7)
    mpl.plot(x3, y3, "mo", label=label3, alpha=0.7)
    mpl.xlabel("x")
    mpl.ylabel("Pn(x)")
    mpl.legend()
    mpl.grid(True)


def diferencas_divididas(n, N, xi, yi, offset):

    for i in range(n):
        N[0][i] = xi[i + offset]

    for i in range(n):
        N[1][i] = yi[i + offset]

    m = n

    for j in range(2, n + 1):

        for k in range(m - 1):
            N[j][k] = (N[j - 1][k + 1] - N[j - 1][k]) / (xi[k + j - 1 + offset] - xi[k + offset])

        m -= 1


def Newton(n, N, xi, x, offset, p):

    res_t = 0

    for i in range(1, n + 1):

        res_p = 1
        for j in range(0, i - 1):

            res_p *= x - xi[j + offset]

        res_t += N[i][0] * res_p

    if p == True:
        print("Newton: P%i (" % (n - 1), x, ") = ", res_t, end="\n\n")

    return res_t


def erro_newton(n, N, xi, x, offset, p):

    res = 1
    for i in range(n + 1):

        if i == n:
            res *= max(abs(N[n + 1]))

        else:
            res *= abs(x - xi[i + offset])

    if p == True:
        print("Erro%i(" % (n - 1), x, ") <=", res, end="\n\n")

    return res


# -----------------------|Calculando as matrizes de diferenças divididas para 17, 3 e 19 pontos|-----------------------#
diferencas_divididas(17, N1, anos, populacao, 0)
diferencas_divididas(3, N2, anos, populacao, 16)
diferencas_divididas(19, N3, anos, populacao, 0)
# ----------------------------------------------------------------------------------------------------------------------#

# -------------------|Calculando as previsões utilizando os polinomios obtidos pelo método de Newton|-------------------#
n1 = Newton(17, N1, anos, 2017, 0, True)
n2 = Newton(17, N1, anos, 2018, 0, True)
n3 = Newton(3, N2, anos, 2019, 16, True)
# ----------------------------------------------------------------------------------------------------------------------#

# ------------|Calculando estimativas dos erros apresentados pelos polinomios obtidos pelo método de Newton|------------#
e1 = erro_newton(17, N3, anos, 2017, 0, True)
e2 = erro_newton(17, N3, anos, 2018, 0, True)
e3 = erro_newton(3, N3, anos, 2019, 16, True)
# ----------------------------------------------------------------------------------------------------------------------#

# ---------------------------------|Plotando os graficos dos polinomios interpoladores|---------------------------------#

# P16(x) -> [2000,2016]
# P2(x) -> [2015,2019]
p_de_x(Newton, 17, N1, anos, xn1, pxn1, 2000, 2016, 0, False)
p_de_x(Newton, 3, N2, anos, xn2, pxn2, 2015, 2019, 16, False)
grafico3(xn1, pxn1, "P16(x)", xn2, pxn2, "P2(x)", anos, populacao, "Pontos de interpolação", "Polinômios de Newton 1")

xn1 = []
pxn1 = []
xn2 = []
pxn2 = []

# P16(x) -> [1999,2018]
# P2(x) -> [1999,2019]
p_de_x(Newton, 17, N1, anos, xn1, pxn1, 1999, 2018, 0, False)
p_de_x(Newton, 3, N2, anos, xn2, pxn2, 1999, 2019, 16, False)
grafico3(xn1, pxn1, "P16(x)", xn2, pxn2, "P2(x)", anos, populacao, "Pontos de interpolação", "Polinômios de Newton 2")

mpl.show()
# ----------------------------------------------------------------------------------------------------------------------#
