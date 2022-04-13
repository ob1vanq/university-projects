# 5. Сформувати вектор відліків часу тривалістю 30 с для частоти дискретизації 512 Гц.
# Сформувати сигнал одиночного прямокутного імпульсу для тривалості імпульсу 0.1, 1, 10 сек.
# (для величин зсуву відносно початку відліку часу 0 та 5 с). Побудувати за допомогою функції plot
# графіки цих 6 сигналів та їх амплітудних і фазових спектрів (функція angle), зробити висновки.
# Графіки будувати для таких частот, щоб було видно особливості спектру.

import numpy as np
import matplotlib.pyplot as plt

from params import c1, c2, spectrum


def impulse(tau: float, long: float, amp=1, fs=512):
    start = int(tau * fs)
    end = int((tau + long) * fs)
    x = np.linspace(0, 30, 30*fs)
    y = np.zeros(30*fs)
    y[start:end] = amp
    return x, y


tau = [0, 5]*3
long = [0.1, 0.1, 1, 1, 10, 10]

fig, axs = plt.subplots(6, 3, figsize=(20, 16))
for i in range(6):
    t, sig = impulse(tau=tau[i], long=long[i])
    axs[i, 0].plot(t, sig, c1)
    axs[i, 1].plot(np.linspace(0, 512 / 2, int(len(sig) / 2)), spectrum(sig), c1)
    axs[i, 2].plot(np.linspace(0, 512 / 2, int(len(sig) / 2)), np.angle(spectrum(sig, phase=True)), c2)
    axs[i, 0].set(title=f"Зсув {tau[i]} с, довжина {long[i]} с, ")
    axs[i, 1].set(title=f"Ампітудний спектр")
    axs[i, 2].set(title=f"Фазовий спектр")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/5.png")
plt.show()
plt.close()

