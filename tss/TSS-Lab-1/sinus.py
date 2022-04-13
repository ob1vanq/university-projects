import matplotlib.pyplot as plt
import numpy as np

def sinus(w, t, a):

    fig, ax = plt.subplots()
    sin = lambda w, t, a: a * np.sin(np.pi * t * w)

    t = np.linspace(0, t, 256)
    y = [sin(w=w, t=i, a=a) for i in t]

    plt.plot(t, y, 'mediumslateblue')
    plt.grid(color = 'grey', linestyle = '--')
    plt.title(f"Частота {w} Гц, Амплітуда {a}")
    ax.set(xlabel="Час, с", ylabel="Амплітуда")
    plt.show()
    return a/2

sinus(10, 10, 10)
