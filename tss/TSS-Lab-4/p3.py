# 3. Сформувати вектор відліків часу тривалістю 3 с для частоти дискретизації 128 Гц.
# Сформувати сигнал ділянки синусоїди частотою 20 Гц.
# Створити розрив (вставити 10 нульових відліків замість відліків сигналу) в сигналі в момент часу 1.05 с.
# Отримати спектр сигналу. Перемістити розрив в момент часу 2 c, розрахувати спектр.
# Побудувати графіки двох сигналів з розривами та їх амплітудних спектрів.
# Зробити висновки щодо того, чи можливо визначити наявність та точне розташування розриву в сигналі,
# аналізуючи спектр сигналу.

import numpy as np
import matplotlib.pyplot as plt

from params import c1, c2, spectrum

fs = 128
t = np.linspace(0, 3, fs*3)
sig = np.sin(2*np.pi*t*20)


def indexes(time: float, fs: int = 128, long: int = 3, n: int = 10):
    start = int(time * fs)
    end = start+n
    return start, end


fig, axs = plt.subplots(2, 2, figsize=(14, 6))

s, e = indexes(1.05)
sig[s:e] = 0
axs[0, 0].plot(t, sig, c1)
axs[0, 1].stem(np.linspace(0, fs / 2, int(len(sig) / 2)), spectrum(sig)*2/(fs/2), linefmt=c2)
axs[0, 0].set(title="Сигнал з розривом у 1.05 с, частота 20 Гц")
axs[0, 1].set(title="Спектр сигналу, частота дискретизації 256 Гц")
s, e = indexes(2)
sig = np.sin(2*np.pi*t*20)
sig[s:e] = 0
axs[1, 0].plot(t, sig, c1)
axs[1, 1].stem(np.linspace(0, fs / 2, int(len(sig) / 2)), spectrum(sig)*2/(fs/2), linefmt=c2)
axs[1, 0].set(title="Сигнал з розривом у 2.0 с, частота 20 Гц")
axs[1, 1].set(title="Спектр сигналу, частота дискретизації 256 Гц")

for ax in axs.flat:
    ax.grid()

plt.tight_layout()
fig.savefig("data/3.png")
plt.show()
plt.close()
