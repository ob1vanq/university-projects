# 2. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 256 Гц.
# Сформувати дискретний аналог сигналу. Побудувати графік автокореляційної функції. Зробити
# висновки щодо характеру АКФ для періодичного сигналу.

import matplotlib.pyplot as plt
import numpy as np

from methods import akf, mirror

t = np.linspace(0, 1, 256)
sig = 5*np.cos(2 * np.pi * t * 50) * 2*np.cos(2 * np.pi * t * 100)

plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
ax[0].plot(t, sig, "b")
ax[1].plot(mirror(t, with_minus=True), mirror(akf(sig)), "b")

ax[0].set(title="$x(t)=5cos(2πt50) + 2cos(2πt100)$")
ax[1].set(title="АКФ сигналу")

for ax in ax.flat:
    ax.grid(color="gray", linestyle="--")
plt.tight_layout()
fig.savefig('data'
            '/2.png')
plt.show()