import numpy as np
import matplotlib.pyplot as mpl
from scipy import interpolate
import time
from prettytable import PrettyTable

# --------------------------------------------|ATENÇÃO|--------------------------------------------#
# Estou usando uma biblioteca chamada: "Prettytable", para deixar a                               #
# tabela com uma aparência bonita.                                                                #
#                                                                                                 #
# Para instalar no windows é só digitar no prompt de comando (admin):                             #
# "pip3 install PTable".                                                                          #
# Para instalar no linux é só digitar no terminal:                                                #
# "sudo pip3 install PTable".                                                                     #
#                                                                                                 #
# -------------------------------------------------------------------------------------------------#

# -------------------------------------|Declaração de funções|-------------------------------------#
def f(x):
    return np.e ** ((-(x ** 2)) / 2) / np.sqrt(2 * np.pi)


def d4f(x):
    return (x ** 4 - 6 * x ** 2 + 3) * np.e ** (-(x ** 2) / 2) / (np.sqrt(2 * np.pi))


def simpson(f, df, x, fx, n, a, b):

    inicio = time.time()

    v = np.linspace(a, b, num=n)

    if n > 1:
        h = abs(v[1] - v[0])

    else:
        h = 0

    x.append(v[0])
    fx.append(f(v[0]))

    res = np.zeros((3))

    for i in range(2, n, 2):

        x.append(v[i - 1])
        x.append(v[i])
        fx.append(f(v[i - 1]))
        fx.append(f(v[i]))

        res[0] += (h / 3) * (fx[i - 2] + 4 * fx[i - 1] + fx[i])

    res[1] = erro(df, n, a, b, h)

    fim = time.time()

    res[2] = fim - inicio

    print("Regra de Simpson:")
    print("\t-> Resultado:", res[0])
    print("\t-> Erro:", res[1])
    print("\t-> Tempo:", res[2], end="\n\n")

    return res


def erro(df, n, a, b, h):

    x0 = np.linspace(a, b, num=1000)

    return (n * (h ** 5) / 180) * np.max(np.abs(d4f(x0)))


def f_de_x(f, fx, x, a, b):

    for i in range(int(a * 50), int(b * 50 + 1)):
        i /= 50

        x.append(i)
        fx.append(f(i))


def grafico_simpson(f, xf, fxs, xs, n, funcao, res):

    mpl.figure()
    mpl.plot(xf, f, label=funcao, color="k")
    mpl.stem(
        xs,
        fxs,
        basefmt="r",
        use_line_collection=True,
        linefmt="red",
        markerfmt=" ",
        label="integração numérica pela Regra de Simpson = %f" % (res),
    )

    for i in range(2, n, 2):
        fxp = []
        xp = []
        fx = interpolate.interp1d(xs[i - 2 : i + 1], fxs[i - 2 : i + 1], kind="quadratic")
        xp = np.linspace(xs[i - 2], xs[i], 50)
        fxp = fx(xp)
        mpl.plot(xp, fxp, color="r")
        mpl.fill_between(xp, fxp, 0, facecolor="#f2600c", alpha=0.3)

    mpl.xlabel("x")
    mpl.ylabel("f(x)")
    mpl.legend()
    mpl.grid(True)


# -------------------------------------------------------------------------------------------------#

# -------------------------------------|Variáveis de controle|-------------------------------------#

# Número de pontos (impar)
n = np.arange(1, 80, 2, dtype=int)

a = 0  # Intervalo inicial
b = np.arange(0, 4, 0.1)  # Intervalos finais

graficos = False
tabela = False
# -------------------------------------------------------------------------------------------------#

xs = []
fxs = []
x = []
fx = []

tab = PrettyTable()
tab.title = "Distribuição Normal"
tab.field_names = ["n", "a", "b", "Integral numérica"]

# ----------------|Calculando a integral numérica com seu erro e tempo de execução|----------------#
for i in range(40):

    print("\nÁrea da distribuição normal entre 0 e %.1f com %i pontos" % (b[i], n[i]), end="\n\n")
    res = simpson(f, d4f, xs, fxs, n[i], a, b[i])

    # ------------------------------------|Plotando os gráficos|-----------------------------------#
    if graficos == True:
        f_de_x(f, fx, x, -4, 4)
        grafico_simpson(fx, x, fxs, xs, n[i], "Distribuição normal de [0,%.1f]" % (b[i]), res[0])
    # ---------------------------------------------------------------------------------------------#

    # ------------------------------|Adicionando os valores à tabela|------------------------------#
    if tabela == True:
        tab.add_row([n[i], a, "%.1f" % (b[i]), res[0]])
    # ---------------------------------------------------------------------------------------------#

    xs = []
    fxs = []
    x = []
    fx = []

# -------------------------------------------------------------------------------------------------#

# ---------------------------------------|Printando a tabela|--------------------------------------#
if tabela == True:
    print(tab)
# -------------------------------------------------------------------------------------------------#

mpl.show()