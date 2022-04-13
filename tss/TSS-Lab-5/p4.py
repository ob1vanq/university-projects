# 4. Для сигналів з п. 2 лабораторної роботи про спектральний аналіз побудувати
# спектрограми:
# – з вікном тривалості 0.1 с та 2 с (без перекриття);
# – з вікном тривалості 1 с з перекриттям 50%.
# Застосувати функцію colorbar для візуалізації значень спектрограми. Зробити
# висновки щодо відображення часових властивостей сигналів у спектрограмі. Порівняти
# інформативність спектрограм та спектрів за Фурьє.
# *Побудувати тривимірні графіки двох різних спектрограм з отриманих.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from params import plot

fs = 256
time = 10
t1 = np.linspace(0, time, time*fs)
s1 = np.sin(2*np.pi*t1*10)
s2 = np.sin(2*np.pi*t1*100)
t2 = np.linspace(0, 2*time, 2*time*fs)
sig_2xs1 = np.append(2*s1, 2*s2)
sig_2xs2 = np.append(2*s2, 2*s1)
sig = [sig_2xs1, sig_2xs2]

fig, axs = plt.subplots(2, 1, figsize=(10, 4))
axs[0].plot(t2, sig_2xs1, plot.color)
axs[0].set_title("Сигнал 1")
axs[1].plot(t2, sig_2xs2, plot.color)
axs[1].set_title("Сигнал 2")
plt.tight_layout()
plot.set_param(axs)
fig.savefig("data/4_1.png")
plt.close()

fig, axs = plt.subplots(3, 2, figsize=(10, 6))
for i in range(2):
    s = sig[i]
    f, t, Sxx = signal.spectrogram(x=s[:int(0.1 * fs)], fs=fs, window='parzen', nperseg=13)
    axs[i, 0].pcolormesh(t, f, Sxx, cmap='PuBu', shading='auto')
    axs[i, 0].set_title(f"Спектрограма сигналу {i+1} (0.1с)")
    f, t, Sxx = signal.spectrogram(x=s[:int(2 * fs)], fs=fs, window='parzen')
    map = axs[i, 1].pcolormesh(t, f, Sxx, cmap='PuBu', shading='auto')
    axs[i, 1].set_title(f"Спектрограма сигналу {i+1} (2с)")
    cbar = plt.colorbar(map, ax=axs[i, 1], ticks=np.linspace(0, 1, 4))
    cbar.set_ticklabels(np.int_(np.linspace(0, 128, 4)))
ax = plt.subplot(313)
s = np.append(s1[:int(0.5*fs)], s2[int(9.5*fs):])
f, t, Sxx = signal.spectrogram(x=s, fs=fs, window='parzen', nperseg=int(fs/4))
ax.pcolormesh(t, f, Sxx, cmap='PuBu', shading='auto')
ax.set_title("Спектрограма з перекриттям 50% (1с)")
plt.tight_layout()
plot.set_param(axs)
fig.savefig("data/4_2.png")
plt.close()


fig = plt.figure(figsize=(10, 10))
f, t, Sxx = signal.spectrogram(x=s1, fs=fs, window='parzen')
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(f[:, None], t[None, :], np.log(Sxx), cmap='PuBu')
ax.plot_wireframe(f[:, None], t[None, :], np.log(Sxx), color="dodgerblue")
fig.savefig("data/4_3.png")
plt.close()

fig = plt.figure(figsize=(10, 10))
f, t, Sxx = signal.spectrogram(x=sig_2xs1, fs=fs, window='parzen')
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(f[:, None], t[None, :], np.log(Sxx), cmap='PuBu')
ax.plot_wireframe(f[:, None], t[None, :], np.log(Sxx), color="dodgerblue")
fig.savefig("data/4_4.png")
plt.close()