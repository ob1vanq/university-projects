# 9. Для довільного сигналу виконати пряме, а потім обернене перетворення Фурьє,
# порівняти початковий сигнал та відновлений сигнал. Знайти середньоквадратичну похибку
# відновлення (функція std). Зробити висновки.

import numpy as np
import matplotlib.pyplot as plt
from params import c1, c2

time = 10
fs = 256
t = np.linspace(0, time, time*fs)
sig = np.sin(2 * np.pi * t * 256)
sig = [i + np.random.normal() for i in sig]

FFT = np.fft.fft(sig)
FFT_real = FFT.real
iFFT = np.fft.ifft(FFT_real).real

fig, axs = plt.subplots(3, 1, figsize=(10, 10))
axs[1].plot(t, sig, c1)
axs[1].set(title="Випадковий сигнал, частота дискретизація 256 Гц")
axs[2].plot(t, iFFT, c2)
axs[2].set(title=f"Відновлений сигнал, середньоквадратична похибка {round(np.std(a=iFFT), 3)}")
axs[0].plot(t, sig, c1)
axs[0].plot(t, iFFT, c2)
axs[0].set(title="Порівняння початкового та відновленого сигналу ")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/9.png")
plt.show()
plt.close()