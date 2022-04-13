# 1. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 256 Гц.
# Сформувати сигнал випадкового білого гаусівського шуму (функція randn). Розрахувати та
# побудувати графік автокореляційної функції. Зробити висновки щодо характеру АКФ для
# шума.

import matplotlib.pyplot as plt
import numpy as np

from methods import akf, mirror

t = np.linspace(0, 1, 256)
noise = np.random.randn(256)

plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
ax[0].plot(t, noise, "b")
ax[1].plot(mirror(t, with_minus=True), mirror(akf(noise)), "b")

ax[0].set(title="Випадковий білий гаусівський шум")
ax[1].set(title="АКФ шуму")

for ax in ax.flat:
    ax.grid(color="gray", linestyle="--")
plt.tight_layout()
fig.savefig('data/1.png')
plt.show()



