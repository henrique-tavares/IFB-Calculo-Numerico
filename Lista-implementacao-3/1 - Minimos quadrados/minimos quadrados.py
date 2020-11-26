import numpy as np
import matplotlib.pyplot as mpl

# -------------------------------------|Declaração de funções|-------------------------------------#
def g0(x):
    return 1


def g1(x):
    return x


def g2(x):
    return x ** 2


def g3(x):
    return x ** 3


def produto_interno(a, b, x, n, tipo):

    res = 0
    if tipo == "f" or tipo == "F":
        for i in range(n):
            res += a(x[i]) * b(x[i])

    elif tipo == "v" or tipo == "V":
        for i in range(n):
            res += a(x[i]) * b[i]

    return res


def g_de_x(gx, x, coeficientes, a, b):

    for i in range(int(a * 200), int(b * 200 + 1)):
        i /= 200

        x.append(i)
        gx[0].append(coeficientes[0][0] + coeficientes[0][1] * i)
        gx[1].append(coeficientes[1][0] + coeficientes[1][1] * i + coeficientes[1][2] * i ** 2)
        gx[2].append(
            coeficientes[2][0] + coeficientes[2][1] * i + coeficientes[2][2] * i ** 2 + coeficientes[2][3] * i ** 3
        )


def erro(x, y, coeficientes):

    v = np.zeros((3))

    for i in range(len(x)):

        v[0] += abs(y[i] - (coeficientes[0][0] + coeficientes[0][1] * x[i])) ** 2
        v[1] += abs(y[i] - (coeficientes[1][0] + coeficientes[1][1] * x[i] + coeficientes[1][2] * (x[i] ** 2))) ** 2
        v[2] += (
            abs(
                y[i]
                - (
                    coeficientes[2][0]
                    + coeficientes[2][1] * x[i]
                    + coeficientes[2][2] * (x[i] ** 2)
                    + coeficientes[2][3] * (x[i] ** 3)
                )
            )
            ** 2
        )

    return v


def grafico4(x, y, xg, g):
    mpl.figure()
    mpl.plot(xg, g[0], label="Aproximação com grau 1", alpha=0.7, color="#eda405")
    mpl.plot(xg, g[1], label="Aproximação com grau 2", alpha=0.7, color="#e30000")
    mpl.plot(xg, g[2], label="Aproximação com grau 3", alpha=0.7, color="#9900ff")
    mpl.plot(x, y, "bo", label="Dados originais", alpha=0.5)
    mpl.xlabel("x")
    mpl.ylabel("y/g1(x)/g2(x)/g3(x)")
    mpl.title("Minimos Quadrados")
    mpl.legend()
    mpl.grid(True)


# -------------------------------------------------------------------------------------------------#

# -----------------------------------|Dados a serem aproximados|-----------------------------------#
x = [1.0, 1.1, 1.3, 1.5, 1.9, 2.1]
y = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]
# -------------------------------------------------------------------------------------------------#

# Variável para controlar o plotamento de gráficos
graficos = True

# ------------------------------------|Declaração de variáveis|------------------------------------#
gx = [[], [], []]
xg = []
g = [g0, g1, g2, g3]

coeficientes = [[], [], []]

minq_a = [[], [], []]
minq_a[0] = np.zeros((2, 2))
minq_a[1] = np.zeros((3, 3))
minq_a[2] = np.zeros((4, 4))

minq_b = [[], [], []]
minq_b[0] = np.zeros((2))
minq_b[1] = np.zeros((3))
minq_b[2] = np.zeros((4))
# -------------------------------------------------------------------------------------------------#

# --------------------------|Calculando as matrizes de produtos internos|--------------------------#
for i in range(3):

    for j in range(2 + i):

        for k in range(2 + i):

            minq_a[i][j][k] = produto_interno(g[j], g[k], x, len(x), "f")

        minq_b[i][j] = produto_interno(g[j], y, x, len(x), "v")

    # Resolvendo o sistema linear atual
    coeficientes[i] = np.linalg.solve(minq_a[i], minq_b[i])
# -------------------------------------------------------------------------------------------------#

# Calculando o erro cometido pelos polinomios através da variancia entre a função e os dados
v = erro(x, y, coeficientes)

# ----------------------|Printando os polinomios com seus respectivos erros|-----------------------#
print("g1(x) = %f +%fx" % (coeficientes[0][0], coeficientes[0][1]))
print("Erro =", v[0], end="\n\n")

print("g2(x) = %f +%fx %fx^2" % (coeficientes[1][0], coeficientes[1][1], coeficientes[1][2]))
print("Erro =", v[1], end="\n\n")

print("g3(x) = %f +%fx +%fx^2 %fx^3" % (coeficientes[2][0], coeficientes[2][1], coeficientes[2][2], coeficientes[2][3]))
print("Erro =", v[2], end="\n\n")
# -------------------------------------------------------------------------------------------------#

# --------------------------------------|Plotando os gráficos|-------------------------------------#
if graficos == True:

    g_de_x(gx, xg, coeficientes, 0.95, 2.15)
    grafico4(x, y, xg, gx)

    gx = [[], [], []]
    xg = []

    g_de_x(gx, xg, coeficientes, -10, 10)
    grafico4(x, y, xg, gx)

    mpl.show()
# -------------------------------------------------------------------------------------------------#
