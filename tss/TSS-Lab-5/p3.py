# 3. Сформувати вектор відліків часу тривалістю 15 с для частоти дискретизації 128 Гц.
# Сформувати сигнали:
# 3.1. синусоїди частотою 40 Гц;
# 3.2. прямокутного імпульсу ширини 1 с в момент часу 10 с;
# 3.3. випадкового сигналу;
# 3.4. суми сигналів 3.1 – 3.3.
# Побудувати спектрограми сигналів за допомогою першого вікна згідно варіанту
# тривалістю 0.2с без використання перекриття вікон. Зробити висновки щодо вигляду спектрограм
# та відповідності часових, спектральних та спектрально-часових властивостей сигналів.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from params import win, impulse, spectrum, plot

time = 15   # sec
fs = 128
t = np.linspace(0, time, time*fs)
sin = np.sin(2*np.pi*t*40)
imp_x, imp_y = impulse(t=15, long=1, fs=fs, tau=10, amp=1)
noise = np.random.rand(time*fs)
sum = sin + imp_y + noise
fig, axs = plt.subplots(4, 2, figsize=(14, 8))
sig = [sin, imp_y, noise, sum]
i = 0
for i in range(4):
    axs[i, 0].plot(t, sig[i])
    f, ts, Sxx = signal.spectrogram(x=(sig[i])[:int(0.21*fs)], fs=fs, window='parzen', nperseg=13)
    axs[i, 1].pcolormesh(ts, f, Sxx, cmap='PuBu', shading='auto')
    i += 1
plot.set_param(axs)
plt.show()
fig.savefig("data/3.png")