import matplotlib.pyplot as mpl
from prettytable import PrettyTable

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


def f(x):
    return -0.1 * x ** 4 - 0.15 * x ** 3 - 0.5 * x ** 2 - 0.25 * x + 1.2


def p(i, x, at, fat):
    res_p = 0
    for j in range(i + 1):
        res_p += x ** j * at[j] / fat[j]
    return res_p


tabela = PrettyTable()
tabela.title = "Polinomios de Taylor"
tabela.field_names = ["i", "x", "P(x)", "f(x)"]

x = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4]
at = [1.2, -0.25, -1, -0.9, -2.4]
fat = [1, 1, 2, 6, 24]
res_t = 0.0
f_x = []
p_0 = []
p_1 = []
p_2 = []
p_3 = []
p_4 = []
i_0 = []

for i in range(11):  # Calculando os valores da f(x) e dos polinômios de Taylor e adicionado-os em tabelas

    for j in range(5):

        res_t += (x[i] ** j) * at[j] / fat[j]
        tabela.add_row([j, x[i], p(j, x[i], at, fat), f(x[i])])

        if abs(res_t - f(x[i])) < 0.001:
            break

    res_t = 0
    print(tabela)
    print("")
    tabela.clear_rows()

for j in range(
    0, 41, 4
):  # Salvando os valores calculados para a f(x) e os polinômios de Taylor para poder plotar os seus graficos

    i = j / 10
    i_0.append(i)
    f_x.append(f(i))
    p_0.append(p(0, i, at, fat))
    p_1.append(p(1, i, at, fat))
    p_2.append(p(2, i, at, fat))
    p_3.append(p(3, i, at, fat))
    p_4.append(p(4, i, at, fat))

mpl.subplot(122)
mpl.plot(i_0, f_x, label="f(x)")
mpl.ylabel("polinomios")
mpl.xlabel("x")
mpl.legend()
mpl.grid(True)
mpl.subplot(121)
mpl.plot(i_0, p_4, label="p4(x)")
mpl.plot(i_0, p_3, label="p3(x)")
mpl.plot(i_0, p_2, label="p2(x)")
mpl.plot(i_0, p_1, label="p1(x)")
mpl.plot(i_0, p_0, label="p0(x)")
mpl.ylabel("polinomios")
mpl.xlabel("x")
mpl.legend()
mpl.grid(True)
mpl.show()
