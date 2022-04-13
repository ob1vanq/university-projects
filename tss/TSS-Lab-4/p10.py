# 10. Побудувати функцію для розрахунку та виводу на графік спектральної густини
# потужності сигналу, прочитаного з файлу. В функцію передавати назву файлу з сигналом та інші
# необхідні дані.
import json

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

fs = 256
t = np.linspace(0, 10, 10 * fs)
sig = np.sin(2*np.pi*t*120) + np.sin(2*np.pi*t*50)

with open("data/sig1.json", "w") as file:
    json.dump(dict(sig=sig.tolist(), fs=fs), file, indent=4)


def periodogram(path):
    from params import c1, c2
    with open(path, "r") as file:
        data = json.load(file)
        sig = data.get("sig")
        fs = data.get("fs")
    time = len(sig)/ fs
    t = np.linspace(0, time, len(sig))
    f, sp = signal.periodogram(sig, fs)
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    axs[0].plot(f, sp, c1)
    axs[0].set(title="Спектральна густина потужності сигналу")
    axs[1].plot(t, sig, c2)
    axs[1].set(title=f"Частота дискретизаціії {fs} Гц")
    for ax in axs.flat:
        ax.grid()
    plt.tight_layout()
    fig.savefig("data/10.png")
    plt.show()
    plt.close()
    return f, sp


periodogram("data/sig1.json")