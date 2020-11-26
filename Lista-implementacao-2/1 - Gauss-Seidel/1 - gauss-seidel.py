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
# Por padrão apenas a tabela do primeiro sistema linear está sendo      #
# printada, pois como a segunda converge, não há porque printa-la.      #
#                                                                       #
# Mas caso deseje vê-la mesmo assim, apenas descomente as linhas:       #
# 76, 77, 88 e 93.                                                      #
#                                                                       #
# -----------------------------------------------------------------------#


def grafico(x1, x2, x3, i):
    mpl.figure()
    mpl.title("Gauss-Seidel")
    mpl.plot(i, np.absolute(x1), label="X1", alpha=0.8)
    mpl.plot(i, np.absolute(x2), label="X2", alpha=0.8)
    mpl.plot(i, np.absolute(x3), label="X3", alpha=0.8)
    mpl.xlabel("Iterações")
    mpl.ylabel("Variáveis")
    mpl.legend()
    mpl.grid(True)


Tabela = PrettyTable()
Tabela.field_names = ["i", "x1", "x2", "x3"]

A1 = [[1, 0, -1], [-0.5, 1, -0.25], [1, -0.5, 1]]  # Primeira matriz
A2 = [[1, 0, -2], [-0.5, 1, -0.25], [1, -0.5, 1]]  # Segunda matriz
b = [0.2, -1.425, 2]  # resultado
x = [0.9, -0.8, 0.7]  # solução
x1 = [[], [], []]
x2 = [[], [], []]
erro = 1e-3
iteracoes_1 = []
iteracoes_2 = []

x1[0].append(10)
x1[1].append(10)
x1[2].append(10)
iteracoes_1.append(0)

x2[0].append(10)
x2[1].append(10)
x2[2].append(10)
iteracoes_2.append(0)

Tabela.title = "Gauss-Seidel (1)"
Tabela.add_row([iteracoes_1[0], x1[0][0], x1[1][0], x1[2][0]])

# --------------------------------------|Aplicando o método de Gauss-Seidel|--------------------------------------#

#   Primeira matriz:
for i in range(300):

    x1[0].append(-((A1[0][1] / A1[0][0]) * x1[1][i]) - ((A1[0][2] / A1[0][0]) * x1[2][i]) + (b[0] / A1[0][0]))
    x1[1].append(-((A1[1][0] / A1[1][1]) * x1[0][i + 1]) - ((A1[1][2] / A1[1][1]) * x1[2][i]) + (b[1] / A1[1][1]))
    x1[2].append(-((A1[2][0] / A1[2][2]) * x1[0][i + 1]) - ((A1[2][1] / A1[2][2]) * x1[1][i + 1]) + (b[2] / A1[2][2]))

    iteracoes_1.append(i + 1)

    # Adicionando os valores atuais a tabela
    Tabela.add_row([iteracoes_1[i + 1], x1[0][i + 1], x1[1][i + 1], x1[2][i + 1]])

    if abs(x1[0][i + 1] - x[0]) < erro and abs(x1[1][i + 1] - x[1]) < erro and abs(x1[2][i + 1] - x[2]) < erro:
        break

print(Tabela)

# Tabela.clear_rows() # Limpando a tabela anterior
# Tabela.title = "Gauss-Seidel (2)"

#   Segunda matriz:
for i in range(300):

    x2[0].append(-((A2[0][1] / A2[0][0]) * x2[1][i]) - ((A2[0][2] / A2[0][0]) * x2[2][i]) + (b[0] / A2[0][0]))
    x2[1].append(-((A2[1][0] / A2[1][1]) * x2[0][i + 1]) - ((A2[1][2] / A2[1][1]) * x2[2][i]) + (b[1] / A2[1][1]))
    x2[2].append(-((A2[2][0] / A2[2][2]) * x2[0][i + 1]) - ((A2[2][1] / A2[2][2]) * x2[1][i + 1]) + (b[2] / A2[2][2]))

    iteracoes_2.append(i + 1)

    # Tabela.add_row([iteracoes_2[i+1], x2[0][i+1], x2[1][i+1], x2[2][i+1]])

    if (abs(x2[0][i + 1] - x[0]) < erro) and (abs(x2[1][i + 1] - x[1]) < erro) and (abs(x2[2][i + 1] - x[2]) < erro):
        break

# print(Tabela)

# ----------------------------------------------------------------------------------------------------------------#

# Plotando os graficos dos valores encontrados através das duas matrizes
grafico(x1[0], x1[1], x1[2], iteracoes_1)
grafico(x2[0], x2[1], x2[2], iteracoes_2)
mpl.show()