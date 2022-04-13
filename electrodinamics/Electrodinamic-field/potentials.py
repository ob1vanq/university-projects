import numpy as np
import copy
from tabulate import tabulate
from timer import ViewProcessing

rs, cs = 3, 6  # основні розміри сітки
k = 6
row, col = rs * k, cs * k  # збільшені розміри сітки
count = 1000 # дефолтна кількість ітерацій
v1 = 0

v2 = float(input("v2 (-0.4) >> "))
v3 = float(input("v3  (2.5) >> "))
v = np.zeros((row, col))
x, y = np.meshgrid(np.linspace(0, 6, col), np.linspace(0, 3, row))


def delta(vb, vc):  # функція перевірки відносного відхиленняя
    minor = (vb - vc)/vc
    m = np.max(minor)
    return m < 0.01


scheme = int(input("Схема номер [1, 2, 3] = "))


def static():  # функція забазпечує незмінність точок стоку, витоку, заслону
    #  0 1 2 3 4 5
    # [0,0,0,0,0,0] 0
    # [0,0,0,0,0,0] 1
    # [0,0,0,0,0,0] 2

    # Variant 1
    if scheme == 1:
        v[0][0:1 * k] = v1
        v[0][2 * k:4 * k] = v2
        v[0][5 * k:6 * k] = v3

    # Variant 2
    if scheme == 2:
        v[0][:] = v3
        v[1 * k][1 * k:2 * k] = v2
        v[1 * k][4 * k:5 * k] = v2
        v[row - 1][:] = v1

    # Variant 3
    if scheme == 3:
        v[0][0:1 * k] = v3
        v[0][2 * k:4 * k] = v3
        v[0][5 * k:6 * k] = v3
        v[1 * k][1 * k:2 * k] = v2
        v[1 * k][4 * k:5 * k] = v2
        v[row - 1][:] = v1


static()
with open("log/loggingV1.html", "w") as file:
    print("Сітка потенціалів початкове наближення:", file=file)
    print(tabulate(v, tablefmt="html"), "\n", file=file)

stop = False
v_before = []
print()
view = ViewProcessing(count, title="Считаю итерации".format())
for a in range(count):
    view.load_line()
    if stop:
        break
    r, c = row - 1, col - 1
    for i in range(row):
        for j in range(col):
            if j == c:
                if i == r:
                    v[i][j] = (2 * v[i][j - 1] + 2 * v[i - 1][j]) / 4
                elif i == 0:
                    v[i][j] = (2 * v[i + 1][j] + 2 * v[i][j - 1]) / 4
                else:
                    v[i][j] = (2 * v[i][j - 1] + v[i + 1][j] + v[i - 1][j]) / 4
            elif j == 0:
                if i == r:
                    v[i][j] = (2 * v[i][j + 1] + 2 * v[i - 1][j]) / 4
                elif i == 0:
                    v[i][j] = (2 * v[i + 1][j] + 2 * v[i][j + 1]) / 4
                else:
                    v[i][j] = (2 * v[i][j + 1] + v[i + 1][j] + v[i - 1][j]) / 4
            else:
                if i == 0:
                    static()
                    v[i][j] = (2 * v[i + 1][j] + v[i][j - 1] + v[i][j + 1]) / 4
                elif i == r:
                    v[i][j] = (2 * v[i - 1][j] + v[i][j - 1] + v[i][j + 1]) / 4
                else:
                    v[i][j] = (v[i][j + 1] + v[i][j - 1] + v[i + 1][j] + v[i - 1][j]) / 4
    if a > 1:
        stop = delta(v_before, v)
    v_before = copy.deepcopy(v)
print()
static()