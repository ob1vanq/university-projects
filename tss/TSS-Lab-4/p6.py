# 6. Сформувати випадковий сигнал тривалістю 10 с для частоти дисктеризації 1000 Гц.
# Побудувати за допомогою функції plot графік сигналу та його амплітудного спектру, зробити
# висновки.

import numpy as np
import matplotlib.pyplot as plt

from params import c1, c2, spectrum

fs = 1000
t = np.linspace(0, 10, 10*fs)
noise = np.random.randn(10*fs)
print(len(noise), np.min(noise), np.max(noise))
fig, axs = plt.subplots(2, 1, figsize=(8, 8))
axs[0].plot(t, noise, c1)
axs[1].plot(np.linspace(0, fs/2, int(len(noise)/2)), spectrum(noise)*4/fs, c2)
axs[0].set_title("Випадковий сигнал")
axs[1].set_title("Спектр випадкового сигналу")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/6.png")
plt.show()
plt.close()