import numpy as np
import matplotlib.pyplot as plt
import colorset
plt.rcParams.update({'font.size': 15})


c1, c2, clr = colorset.colors.random(2, grid=True)
# c1, c2, clr = 'mediumslateblue', 'dodgerblue', 'dimgray'
linestyle = "--"


def phase_velocity(freq_10, freq_20, f_10_2c, f_20_2c):
    c = 2.998
    freq_10 /= 1e9
    freq_20 /= 1e9
    f_10_2c /= 1e9
    f_20_2c /= 1e9
    freq = lambda f: np.linspace(f+0.001, f*4, 1000)
    f1 = freq(freq_10)
    f2 = freq(freq_20)
    vf1 = c/np.sqrt(1 - (freq_10/f1)**2)
    vf2 = c/np.sqrt(1 - (freq_20/f2)**2)
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(f1, vf1, c1, lw=2)
    ax.plot(f2, vf2, c2, lw=2)
    ax.set(title="Залежність фазової швидкості від частоти",
           xlabel="Частота, ГГц",
           ylabel="Фазова швидкість, $10^{8}$ м/с")
    ax.set_ylim(0, 15)
    ax.set_xlim(freq_10/2, freq_20*2)


    ax.axhline(c, color=clr, linestyle=linestyle)
    ax.axhline(2*c, color=clr, linestyle=linestyle)

    ax.axvline(freq_10, color=clr, linestyle=linestyle)
    ax.axvline(f_10_2c, color=clr, linestyle=linestyle)
    ax.axvline(freq_20, color=clr, linestyle=linestyle)
    ax.axvline(f_20_2c, color=clr, linestyle=linestyle)

    txt = ['f$^{10}_{кp}$', 'f$^{10}_{2c}$', 'f$^{20}_{кp}$', 'f$^{20}_{2c}$']
    diapazon = [freq_10, f_10_2c, freq_20, f_20_2c]
    for i in range(4):
        ax.text(diapazon[i]+0.05, 0.5, txt[i])
    ax.legend(['f$^{10}_{кp}$', 'f$^{10}_{2c}$'])

    ax.grid(color="gray")
    plt.tight_layout()
    fig.savefig("data/1.png")
    plt.show()


def power(K):

    z = np.linspace(0, 6, 1000)
    P = 0.1*np.log(np.exp(-2*K*z))
    p = -30
    ind = np.argwhere(np.diff(np.sign(p-P))).flatten()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(z, P, c1)
    ax.axvline(z[ind[0]], color=clr, linestyle=linestyle)
    ax.axhline(p, color=clr, linestyle=linestyle)
    ax.set(title="Залежність потужності вищої моди у дБ від відстані",
           xlabel="Відстань z, cм",
           ylabel="Потужність P, дБ")
    ax.grid(color="gray")
    plt.tight_layout()
    fig.savefig("data/2.png")
    # plt.show()



    return z[ind[0]]


def fields(a, b, L, l):
    L = np.round(L*1e3, 1)
    l = np.round(l*1e3, 1)
    fs = 30
    a *= 1e3
    b *= 1e3
    Zc = 120*np.pi
    K = np.round(2 * np.pi / L, 4)
    x = np.linspace(0, a, fs)
    y = np.linspace(0, b, fs)
    z = np.linspace(0, L, fs)
    size = (x.size, z.size)
    Ex, Ey, Ez = np.zeros(size), np.zeros(size), np.zeros(size)
    Hx, Hy, Hz = np.zeros(size), np.zeros(size), np.zeros(size)
    Px, Py, Pz = np.zeros(size), np.zeros(size), np.zeros(size)
    for i in range(0, x.size):
        for j in range(0, z.size):
            Ey[i, j] = Zc*(2*a/l)*np.sin(np.pi*x[i]/a)*np.cos(-K*z[j])
            Hx[i, j] = -(2 * a / L) * np.sin(np.pi * x[i] / a) * np.cos(-K *z[j])
            Hz[i, j] = -np.cos(np.pi*x[i]/a)*np.sin(-K*z[j])
            Px[i, j] = Ey[i, j] * Hz[i, j] - Ez[i, j] * Hy[i, j]
            Py[i, j] = Ez[i, j] * Hx[i, j] - Ex[i, j] * Hz[i, j]
            Pz[i, j] = Ex[i, j] * Hy[i, j] - Ey[i, j] * Hx[i, j]
    front = np.meshgrid(x, y)
    x_side, y_side = np.meshgrid(z, x)
    top = np.meshgrid(z, y)
    fig, (xy, zx, zy) = plt.subplots(3, 1, figsize=(14, 18))
    xy.quiver(*front, Ey, Ex, color=c1)
    xy.quiver(*front, Hx, Hy, color=c2)
    zx.quiver(x_side, y_side, Ez, Ex, color=c1)
    zx.quiver(x_side, y_side, Hz, Hx, color=c2)
    zy.quiver(*top, Ez, Ey,  color=c1)
    zy.quiver(*top, Hz, Hy,   color=c2)
    x_lab = ["x, мм", "z, мм", "z, мм"]
    y_lab = ["y, мм", "x, мм", "y, мм"]
    for ax, i in zip((xy, zx, zy), range(3)):
        ax.set(title=f"Розподіл полів в площині {x_lab[i][0]}{y_lab[i][0]} хвилевода",xlabel=x_lab[i], ylabel=y_lab[i])
        ax.legend(["E", "H"])
    plt.tight_layout()
    fig.savefig("data/3.png")
    plt.close()

    fig, (pzx, pzy, azx, azy) = plt.subplots(4, 1, figsize=(14, 24))
    pzx.quiver(x_side, y_side, Pz, Px, color=c1)
    pzy.quiver(*top, Pz, Py, color=c1)
    azx.quiver(x_side, y_side, -Hx, Hz, color=c2)
    azy.quiver(*top, -Hz, Hy, color=c2)
    x_lab = ["z, мм", "z, мм", "z, мм", "z, мм"]
    y_lab = ["x, мм", "y, мм", "x, мм", "y, мм"]
    title = ["Розподіл вектора Пойнтінга в площині zx",
             "Розподіл вектора Пойнтінга в площині zy",
             "Розподіл густини електричного струму у площині zx",
             "Розподіл густини електричного струму у площині zy"]
    for ax, i in zip((pzx, pzy, azx, azy), range(4)):
        ax.set(title=title[i], xlabel=x_lab[i], ylabel=y_lab[i])
    plt.tight_layout()
    fig.savefig("data/4.png")
    plt.close()

 