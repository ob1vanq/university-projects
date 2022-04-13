import numpy as np


def var():
    epsilon = np.append([2.26] * 5, [2] * 5)
    f = np.append([1e+9] * 5, [2e+9] * 5)
    d = [1.37, 2.7, 0.72, 1.2, 1.35, 0.73, 1.54, 0.41, 0.85, 1.3]
    D = [4.6, 9.0, 4.6, 7.3, 9.0, 2.2, 4.6, 2.2, 4.6, 7.3]
    l = [40, 60, 80, 100, 120, 20, 30, 40, 60, 80]
    ZH = [50 + 50j, 50 + 50j, 50 - 50j, 50 - 50j, 25 + 25j, 25 + 25j, 25 - 25j, 25 - 25j, 100, 100]

    n = int(input("Номер варіанту >> "))
    print(n)
    n = n % 10
    N = n-1
    print(f"epsilon = {epsilon[N]}\nf = {f[N]}\nd = {d[N]}\nD = {D[N]}\nl = {l[N]}\nZH = {ZH[N]}\n")
    return epsilon[N], f[N], d[N], D[N], l[N], ZH[N]


eps, f, d, D, l , Zn = var()