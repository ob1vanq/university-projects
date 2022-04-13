# 11. Побудувати функцію, яка дозволяє розрахувати та побудувати амплітудний та фазовий
# спектр фрагменту довільного сигналу.

import numpy as np
import matplotlib.pyplot as plt
from params import c1, c2

fs = 1000
f1, f2 = 120, 50
t = np.linspace(0, 1, 1 * fs)
sig = np.sin(2*np.pi*t*f1) + np.sin(2*np.pi*t*f2) + np.random.rand(1*fs)


def spectrum(signal):
    size = int(len(signal)/2)
    amp = abs(np.fft.fft(signal).real)
    phase = np.angle(np.fft.fft(signal))
    return amp[:size], phase[:size], size


fig, axs = plt.subplots(3, 1, figsize=(14, 10))
amp, phase, size = spectrum(sig)
axs[0].plot(t, sig, c1)
axs[1].plot(np.linspace(0, fs/2, size), amp, c1)
axs[2].plot(np.linspace(0, fs/2, size), phase, c2)
axs[0].set(title=f"Сигнал з частотами {f1}, {f2} Гц, частота дискретиації {fs} Гц")
axs[1].set(title=f"Ампітудний спектр")
axs[2].set(title=f"Фазовий спектр")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/11.png")
plt.show()
plt.close()