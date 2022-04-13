import numpy as np
from scipy import signal
from p1 import a, b, c1, c2
import matplotlib.pyplot as plt


def plot(t, y1, y2, title):
    fig, ax = plt.subplots(2, 1, figsize=(6, 6))
    ax[0].plot(t, y1, c1)
    ax[1].plot(t, y2, c2)
    for axis in ax.flat:
        axis.grid(linestyle="--")
        axis.set(xlabel="t, с", ylabel="амплітуда")
    fig.savefig(f"data/point 4_{title}.png")
    plt.show()
    plt.close()


t = np.linspace(0, 1, 1000)
sin3 = np.sin(2*np.pi*3*t)
sin20 = np.sin(2*np.pi*20*t)
sin_add = sin3 + sin20
y_add = signal.lfilter(b, a, x=sin_add)

y1 = signal.lfilter(b, a, x=sin3)
y2 = signal.lfilter(b, a, x=sin20)
y3 = y1 + y2
plot(t, y_add, y3, "1")

y_odn1 = signal.lfilter(b, a, x=sin3) * 12
sin3 = sin3 * 12
y_odn2 = signal.lfilter(b, a, x=sin3)
plot(t, y_odn1, y_odn2, "2")
