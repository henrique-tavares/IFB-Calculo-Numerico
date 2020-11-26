import numpy as np
import matplotlib.pyplot as mpl
from prettytable import PrettyTable

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


def p_de_x(a, x):

    res = 0

    for i in range(4):
        res += a[i] * x ** i

    return res


def p_de_x_graf(a, b, c):

    for i in range(a * 10, (b * 10) + 1):
        i /= 10
        graf_x.append(i)
        graf_y.append(p_de_x(c, i))


def grafico(x1, y1, x2, y2):
    mpl.figure()
    mpl.title("Polinomio por interpolação com sistema linear")
    mpl.plot(x1, y1, label="P3(x)")
    mpl.plot(x2, y2, "ro", alpha=0.6, label="Pontos de interpolação")
    mpl.xlabel("x")
    mpl.ylabel("P3(x)")
    mpl.legend()
    mpl.grid(True)
    mpl.show()


x = [-2, 0, 1, 2]
y = [-162, 0, 21, 242]
a = []
graf_x = []
graf_y = []

V = np.zeros((4, 4), dtype=float)
M = np.zeros((4, 5), dtype=float)

# -------------------------|Montando a matriz de Vandermonde|-------------------------#
for i in range(4):

    for j in range(4):

        V[i][j] = x[i] ** j
# ------------------------------------------------------------------------------------#

# Printando a matriz de Vandermonde
print("Matriz de Vandermonde:")
print(np.matrix(V), end="\n\n")

# --------------------|Montando a matriz aumentada de Vandermonde|--------------------#
for i in range(4):

    for j in range(5):

        if j == 4:
            M[i][j] = y[i]
        else:
            M[i][j] = V[i][j]
# ------------------------------------------------------------------------------------#

# ----------------------|Aplicando a eliminação de Gauss-Jordan|----------------------#

#   (->) Indo:
for i in range(3):

    for j in range(i + 1, 4):

        pivo = M[j][i] / M[i][i]

        for k in range(5):

            M[j][k] += -pivo * M[i][k]

#   (<-) Voltando:
for i in range(3, -1, -1):

    if M[i][i] != 1:
        M[i][4] /= M[i][i]
        M[i][i] /= M[i][i]

    for j in range(i - 1, -1, -1):

        pivo = M[j][i] / M[i][i]

        for k in range(5):

            M[j][k] += -pivo * M[i][k]
# ------------------------------------------------------------------------------------#

# Colocando os coeficientes em um novo vetor
for i in range(4):
    a.append(M[i][4])

# Printando os coeficientes do polinomio interpolador
print("Coeficientes do polinomio P3(x):")
print(a, end="\n\n")

# Printando o polinomio interpolador
print("P3(x) = (%.1f)x + (%.1f)x^2 + (%.1f)x^3\n" % (a[1], a[2], a[3]))

# Calculando valores utilizando o polinomio interpolador
print("P3(-2) =", p_de_x(a, -2), "\n")
print("P3(0) =", p_de_x(a, 0), "\n")
print("P3(1) =", p_de_x(a, 1), "\n")
print("P3(2) =", p_de_x(a, 2), "\n\n")
print("P3(-1) =", p_de_x(a, -1), "\n")
print("P3(3) =", p_de_x(a, 3), "\n")

# Plotando o grafico do polinomio interpolador
p_de_x_graf(-4, 4, a)
grafico(graf_x, graf_y, x, y)