# 4. Сформувати вектор відліків часу тривалістю 3 с для частоти дискретизації 512 Гц.
# Сформувати сигнал послідовності прямокутних імпульсів з частотою 10 та 100 Гц. Побудувати
# за допомогою функції plot графіки сигналів та їх амплітудних спектрів, зробити висновки.
# Графіки будувати для таких частот, щоб було видно особливості спектру
# (вивести на графік частину спектру на нижніх частотах).

import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt

from params import c1, c2, spectrum

fs = 512
t = np.linspace(0, 3, fs*3)
sig_10 = square(2*np.pi*t*10)
sig_100 = square(2*np.pi*t*100)
signals = [sig_10, sig_100]
fig, axs = plt.subplots(2, 2, figsize=(25, 8))
signals_name = ["10", "100"]

for i in range(2):
    axs[i, 0].plot(t, signals[i], c1)
    axs[i, 0].set(title="Сигнал з частотою " + signals_name[i])
    axs[i, 1].plot(np.linspace(0, 512/2, int(len(signals[i])/2)), spectrum(signals[i])*2/(fs/2), c2)
    axs[i, 1].set(title="Спектр сигналу, частота дискретизації 512 Гц")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/4.png")
plt.show()
plt.close()

