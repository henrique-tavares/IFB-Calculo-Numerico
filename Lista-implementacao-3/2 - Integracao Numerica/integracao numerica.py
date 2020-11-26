import numpy as np
import matplotlib.pyplot as mpl
from scipy import interpolate
import time

# -------------------------------------|Declaração de funções|-------------------------------------#
def f0(x):
    return np.e ** np.cos(np.pi * x)


def d2f0(x):
    return np.pi ** 2 * (np.sin(np.pi * x) ** 2 - np.cos(np.pi * x)) * np.e ** (np.cos(np.pi * x))


def d4f0(x):
    return (
        np.pi ** 4
        * (
            np.sin(np.pi * x) ** 4
            - 6 * np.sin(np.pi * x) ** 2 * np.cos(np.pi * x)
            - 4 * np.sin(np.pi * x) ** 2
            + 3 * np.cos(np.pi * x) ** 2
            + np.cos(np.pi * x)
        )
        * np.e ** (np.cos(np.pi * x))
    )


def f1(x):
    return np.sin(np.pi * x ** 2)


def d2f1(x):
    return 2 * np.pi * (-2 * np.pi * x ** 2 * np.sin(np.pi * x ** 2) + np.cos(np.pi * x ** 2))


def d4f1(x):
    return (
        4
        * np.pi ** 2
        * (
            4 * np.pi ** 2 * x ** 4 * np.sin(np.pi * x ** 2)
            - 12 * np.pi * x ** 2 * np.cos(np.pi * x ** 2)
            - 3 * np.sin(np.pi * x ** 2)
        )
    )


def f2(x):
    return 1 / (1 + x ** 5)


def d2f2(x):
    return 10 * x ** 3 * (5 * x ** 5 / (x ** 5 + 1) - 2) / (x ** 5 + 1) ** 2


def d4f2(x):
    return (
        120
        * x
        * (125 * x ** 15 / (x ** 5 + 1) ** 3 - 150 * x ** 10 / (x ** 5 + 1) ** 2 + 40 * x ** 5 / (x ** 5 + 1) - 1)
        / (x ** 5 + 1) ** 2
    )


def f2_g(x):
    if x != -1:
        return 1 / (1 + x ** 5)


def f3(x):
    return np.cos(np.e ** np.cos(np.pi * x))


def d2f3(x):
    return (
        np.pi ** 2
        * (
            -np.e ** (np.cos(np.pi * x)) * np.sin(np.pi * x) ** 2 * np.cos(np.e ** (np.cos(np.pi * x)))
            - np.sin(np.pi * x) ** 2 * np.sin(np.e ** (np.cos(np.pi * x)))
            + np.sin(np.e ** (np.cos(np.pi * x))) * np.cos(np.pi * x)
        )
        * np.e ** (np.cos(np.pi * x))
    )


def d4f3(x):
    return (
        np.pi ** 4
        * (
            np.e ** (3 * np.cos(np.pi * x)) * np.sin(np.pi * x) ** 4 * np.cos(np.e ** (np.cos(np.pi * x)))
            + 6 * np.e ** (2 * np.cos(np.pi * x)) * np.sin(np.pi * x) ** 4 * np.sin(np.e ** (np.cos(np.pi * x)))
            - 6
            * np.e ** (2 * np.cos(np.pi * x))
            * np.sin(np.pi * x) ** 2
            * np.sin(np.e ** (np.cos(np.pi * x)))
            * np.cos(np.pi * x)
            - 7 * np.e ** (np.cos(np.pi * x)) * np.sin(np.pi * x) ** 4 * np.cos(np.e ** (np.cos(np.pi * x)))
            + 18
            * np.e ** (np.cos(np.pi * x))
            * np.sin(np.pi * x) ** 2
            * np.cos(np.pi * x)
            * np.cos(np.e ** (np.cos(np.pi * x)))
            + 4 * np.e ** (np.cos(np.pi * x)) * np.sin(np.pi * x) ** 2 * np.cos(np.e ** (np.cos(np.pi * x)))
            - 3 * np.e ** (np.cos(np.pi * x)) * np.cos(np.pi * x) ** 2 * np.cos(np.e ** (np.cos(np.pi * x)))
            - np.sin(np.pi * x) ** 4 * np.sin(np.e ** (np.cos(np.pi * x)))
            + 6 * np.sin(np.pi * x) ** 2 * np.sin(np.e ** (np.cos(np.pi * x))) * np.cos(np.pi * x)
            + 4 * np.sin(np.pi * x) ** 2 * np.sin(np.e ** (np.cos(np.pi * x)))
            - 3 * np.sin(np.e ** (np.cos(np.pi * x))) * np.cos(np.pi * x) ** 2
            - np.sin(np.e ** (np.cos(np.pi * x))) * np.cos(np.pi * x)
        )
        * np.e ** (np.cos(np.pi * x))
    )


def trapezio(f, df, x, fx, n, a, b):

    inicio = time.time()

    v = np.linspace(a, b, num=n)
    h = abs(v[1] - v[0])

    x.append(v[0])
    fx.append(f(v[0]))

    res = np.zeros((3))

    for i in range(1, n):

        x.append(v[i])
        fx.append(f(v[i]))

        res[0] += (h / 2) * (fx[i - 1] + fx[i])

    res[1] = erro(df, n, a, b, h, "T")

    fim = time.time()

    res[2] = fim - inicio

    print("Regra dos Trapezios:")
    print("\t-> Resultado:", res[0])
    print("\t-> Erro:", res[1])
    print("\t-> Tempo:", res[2], end="\n\n")

    return res


def simpson(f, df, x, fx, n, a, b):

    inicio = time.time()

    v = np.linspace(a, b, num=n)
    h = abs(v[1] - v[0])

    x.append(v[0])
    fx.append(f(v[0]))

    res = np.zeros((3))

    for i in range(2, n, 2):

        x.append(v[i - 1])
        x.append(v[i])
        fx.append(f(v[i - 1]))
        fx.append(f(v[i]))

        res[0] += (h / 3) * (fx[i - 2] + 4 * fx[i - 1] + fx[i])

    res[1] = erro(df, n, a, b, h, "S")

    fim = time.time()

    res[2] = fim - inicio

    print("Regra de Simpson:")
    print("\t-> Resultado:", res[0])
    print("\t-> Erro:", res[1])
    print("\t-> Tempo:", res[2], end="\n\n")

    return res


def erro(df, n, a, b, h, tipo):

    x0 = np.linspace(a, b, num=1000)

    if tipo == "t" or tipo == "T":
        return (n * (h ** 3) / 12) * np.max(np.abs(df(x0)))

    elif tipo == "s" or tipo == "S":
        return (n * (h ** 5) / 180) * np.max(np.abs(df(x0)))


def f_de_x(f, fx, x, a, b):

    for i in range(int(a * 50), int(b * 50 + 1)):
        i /= 50

        x.append(i)
        fx.append(f(i))


def grafico_trapezio(f, xf, t, xt, funcao):

    mpl.figure()
    mpl.plot(xf, f, label=funcao, color="k")
    mpl.stem(
        xt,
        t,
        basefmt="b",
        use_line_collection=True,
        linefmt="blue",
        markerfmt="blue",
        label="integração numérica pela Regra dos Trapézios",
    )
    mpl.fill_between(xt, t, 0, facecolor="#8112ff", alpha=0.3)
    mpl.xlabel("x")
    mpl.ylabel("f(x)")
    mpl.legend()
    mpl.grid(True)


def grafico_simpson(f, xf, fxs, xs, funcao):

    mpl.figure()
    mpl.plot(xf, f, label=funcao, color="k")
    mpl.stem(
        xs,
        fxs,
        basefmt="r",
        use_line_collection=True,
        linefmt="red",
        markerfmt=" ",
        label="integração numérica pela Regra de Simpson",
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
n = 1000001

a = 0  # Intervalo inicial
b = 1  # Intervalo final

funcao0 = False
funcao1 = False
funcao2 = False
funcao3 = True

graficos = False
# -------------------------------------------------------------------------------------------------#

# ------------------------------------|Declaração de variáveis|------------------------------------#
f = [f0, f1, [f2, f2_g], f3]
df = [[d2f0, d4f0], [d2f1, d4f1], [d2f2, d4f2], [d2f3, d4f3]]
xt = [[], [], [], []]
fxt = [[], [], [], []]
xs = [[], [], [], []]
fxs = [[], [], [], []]
x = [[], [], [], []]
fx = [[], [], [], []]
# -------------------------------------------------------------------------------------------------#


# Caso n seja par, incrementa-se 1, pois n precisa de ser ímpar
if n % 2 == 0:
    n += 1

# --|Calculando e printando as integrais numéricas com seus respectivos erros e tempo de execução|--#
if funcao0 == True:
    print("\nÁrea de e^cos(pi*x) entre", a, "e", b, "com", n, "pontos", end="\n\n")
    trapezio(f[0], df[0][0], xt[0], fxt[0], n, a, b)
    simpson(f[0], df[0][1], xs[0], fxs[0], n, a, b)

if funcao1 == True:
    print("\nÁrea de sen(pi*x^2) entre", a, "e", b, "com", n, "pontos", end="\n\n")
    trapezio(f[1], df[1][0], xt[1], fxt[1], n, a, b)
    simpson(f[1], df[1][1], xs[1], fxs[1], n, a, b)

if funcao2 == True:
    print("\nÁrea de 1/(1 + x^5) entre", a, "e", b, "com", n, "pontos", end="\n\n")
    trapezio(f[2][0], df[2][0], xt[2], fxt[2], n, a, b)
    simpson(f[2][1], df[2][1], xs[2], fxs[2], n, a, b)

if funcao3 == True:
    print("\nÁrea de cos(e^cos(pi*x)) entre", a, "e", b, "com", n, "pontos", end="\n\n")
    trapezio(f[3], df[3][0], xt[3], fxt[3], n, a, b)
    simpson(f[3], df[3][1], xs[3], fxs[3], n, a, b)
# -------------------------------------------------------------------------------------------------#

# --------------------------------------|Plotando os gráficos|-------------------------------------#
if graficos == True:

    if funcao0 == True:
        f_de_x(f[0], fx[0], x[0], -2, 2)
        grafico_trapezio(fx[0], x[0], fxt[0], xt[0], "e^cos(pi*x)")
        grafico_simpson(fx[0], x[0], fxs[0], xs[0], "e^cos(pi*x)")

    if funcao1 == True:
        f_de_x(f[1], fx[1], x[1], -2, 2)
        grafico_trapezio(fx[1], x[1], fxt[1], xt[1], "sen(pi*x^2)")
        grafico_simpson(fx[1], x[1], fxs[1], xs[1], "sen(pi*x^2)")

    if funcao2 == True:
        f_de_x(f[2][1], fx[2], x[2], -2, 2)
        grafico_trapezio(fx[2], x[2], fxt[2], xt[2], "1/(1 + x^5)")
        grafico_simpson(fx[2], x[2], fxs[2], xs[2], "1/(1 + x^5)")

    if funcao3 == True:
        f_de_x(f[3], fx[3], x[3], -2, 2)
        grafico_trapezio(fx[3], x[3], fxt[3], xt[3], "cos(e^cos(pi*x))")
        grafico_simpson(fx[3], x[3], fxs[3], xs[3], "cos(e^cos(pi*x))")

    mpl.show()
# -------------------------------------------------------------------------------------------------#
