import numpy as np
from tabulate import tabulate

from potentials import row, col, k, v

Ex, Ey = np.zeros((row, col)), np.zeros((row, col))

for i in range(row):
    for j in range(col):
        if j == 0 or j == col - 1:
            if i == 0 or i == row - 1:
                Ex[i][j] = Ey[i][j] = 0
            else:
                Ey[i][j] = (v[i - 1][j] - v[i + 1][j]) / (2 * (1 / k))
                Ex[i][j] = 0
        elif i == row - 1 and j < col:
            if j == 0 or j == col - 1:
                Ex[i][j] = Ey[i][j] = 0
            else:
                Ex[i][j] = (v[i][j - 1] - v[i][j + 1]) / (2 * (1 / k))
                Ey[i][j] = 0
        elif i == 0:
            if j == 0 or j == col:
                Ex[i][j] = Ey[i][j] = 0
            else:
                Ex[i][j] = (v[i][j - 1] - v[i][j + 1]) / (2 * (1 / k))
                Ey[i][j] = 0
        else:
            Ey[i][j] = (v[i - 1][j] - v[i + 1][j]) / (2 * (1 / k))
            Ex[i][j] = (v[i][j - 1] - v[i][j + 1]) / (2 * (1 / k))


with open("log/loggingV2.html", "w") as file:
    print("Сітка потенціалів:\n", file=file)
    print(tabulate(np.round(v, 2), tablefmt="html"), "\n", file=file)
with open("log/loggingE.html", "w") as file:
    print("Сітка Ex:\n", file=file)
    print(tabulate(np.round(Ex, 2), tablefmt="html"), "\n", file=file)
    print("Сітка  Ey:\n", file=file)
    print(tabulate(np.round(Ey, 2), tablefmt="html"), "\n", file=file)