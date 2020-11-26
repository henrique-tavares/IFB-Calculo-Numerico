import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as mpl

# --------------------------------ATENÇÃO--------------------------------#
# Estou usando uma biblioteca chamada: "Prettytable", para deixar a     #
# tabela com uma aparência bonita.                                      #
#                                                                       #
# Para instalar no windows é só digitar no prompt de comando (admin):   #
# "pip3 install PTable".                                                #
# Para instalar no linux é só digitar no terminal:                      #
# "sudo pip3 install PTable".                                           #
#                                                                       #
# -----------------------------------------------------------------------#

tabela2 = PrettyTable()
tabela2.title = "Valores dos Polinnmios de Taylor"
tabela2.field_names = ["i", "x", "p0(x)", "p1(x)", "p2(x)", "p3(x)", "p4(x)", "f(x)"]

tabela3 = PrettyTable()
tabela3.title = "Diferenca entre os Polinomios de Taylor e a funcao original"
tabela3.field_names = ["i", "x", "p0(x)-f(x)", "p1(x)-f(x)", "p2(x)-f(x)", "p3(x)-f(x)", "p4(x)-f(x)"]

tabela4 = PrettyTable()
tabela4.title = "Aproximacao do primeiro ponto distante do Polinomio de Taylor em relacao a funcao original, usando o metodo da bisseccao"
tabela4.field_names = ["i", "x0", "xk", "xb", "h(xb)", "pi(xb)", "f(xb)"]


def f(x):

    return -0.1 * x ** 4 - 0.15 * x ** 3 - 0.5 * x ** 2 - 0.25 * x + 1.2


def p(i, x, at, fat):

    res_p = 0
    for j in range(i + 1):
        res_p += x ** j * at[j] / fat[j]
    return res_p


def h(x, y):

    return y - f(x) - 0.001


def bisseccao(x0, xk, i, xv, pxv, fxv):

    xb0 = x0
    xbk = xk

    for j in range(1000):

        xm = (x0 + xk) / 2

        xv.append(xm)
        pxv.append(p(i, xm, at, fat))
        fxv.append(f(xm))

        tabela4.add_row([j + 1, x0, xk, xm, h(xm, p(i, xm, at, fat)), p(i, xm, at, fat), f(xm)])

        if abs(h(xm, p(i, xm, at, fat))) < 0.0001:
            print(tabela4)
            tabela4.clear_rows()
            break

        else:
            if (np.sign(h(x0, p(i, x0, at, fat))) * np.sign(h(xm, p(i, xm, at, fat)))) < 0:
                xk = xm
            else:
                x0 = xm


def grafico(fx, fy, px, py, xb, pxb, fxb):

    mpl.figure()
    mpl.plot(px, py, color="m", label="pi(x)")
    mpl.plot(fx, fy, color="k", label="f(x)", linestyle="dashed")
    mpl.plot(xb, pxb, "ro", label="x -> pi(x)")
    mpl.plot(xb, fxb, "bo", label="x -> f(x)")
    mpl.xlabel("x")
    mpl.ylabel("f(x)/pi(x)")
    mpl.legend()
    mpl.grid(True)


x = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4]
at = [1.2, -0.25, -1, -0.9, -2.4]
fat = [1, 1, 2, 6, 24]
fx = []
p0 = []
p1 = [1.2]
p2 = [1.2]
p3 = [1.2]
p4 = [1.2]
res_t = 0
res_f = 0
x0 = 0
xk = 0
xm = 0
xb0 = 0
xbk = 0
i_0 = []
f_x = []
p_0 = []
p_1 = []
p_2 = []
p_3 = []
p_4 = []
xb0 = []
xb1 = []
xb2 = []
xb3 = []
fxb0 = []
fxb1 = []
fxb2 = []
fxb3 = []
pxb0 = []
pxb1 = []
pxb2 = []
pxb3 = []

for i in range(11):  # Calculando os valores da f(x) e dos polinômios de Taylor e salvando-os em vetores

    fx.append(f(x[i]))

    for j in range(5):

        res_t = p(j, x[i], at, fat)

        if j == 0:
            p0.append(res_t)
        elif j == 1:
            p1.append(res_t)
        elif j == 2:
            p2.append(res_t)
        elif j == 3:
            p3.append(res_t)
        elif j == 4:
            p4.append(res_t)

        if abs(res_t - f(x[i])) < 0.001:
            break

    res_t = 0

for i in range(11):  # Adicionando os valores calculados anteriormente as tabelas

    tabela2.add_row([i, x[i], p0[i], p1[i], p2[i], p3[i], p4[i], fx[i]])
    tabela3.add_row([i, x[i], p0[i] - fx[i], p1[i] - fx[i], p2[i] - fx[i], p3[i] - fx[i], p4[i] - fx[i]])

for j in range(
    0, 41, 4
):  # Salvando os valores calculados para a f(x) e os polinômios de Taylor para poder plotar os seus graficos

    i = j / 100
    i_0.append(i)
    f_x.append(f(i))
    p_0.append(p(0, i, at, fat))
    p_1.append(p(1, i, at, fat))
    p_2.append(p(2, i, at, fat))
    p_3.append(p(3, i, at, fat))
    p_4.append(p(4, i, at, fat))

print(tabela2)
print("")
print(tabela3)
print("")

bisseccao(x[0], x[1], 0, xb0, pxb0, fxb0)
grafico(i_0, f_x, i_0, p_0, xb0, pxb0, fxb0)

bisseccao(x[0], x[1], 1, xb1, pxb1, fxb1)
grafico(i_0, f_x, i_0, p_1, xb1, pxb1, fxb1)

bisseccao(x[0], x[1], 2, xb2, pxb2, fxb2)
grafico(i_0, f_x, i_0, p_2, xb2, pxb2, fxb2)

bisseccao(x[0], x[1], 3, xb3, pxb3, fxb3)
grafico(i_0, f_x, i_0, p_3, xb3, pxb3, fxb3)

mpl.show()